import asyncio, ssl, certifi, logging, os
import aiomqtt

logging.basicConfig(format='%(asctime)s - cliente mqtt - %(levelname)s:%(message)s', level=logging.INFO, datefmt='%d/%m/%Y %H:%M:%S %z')

async def topico1_consumer(): #crea una tarea que escucha el topico 1
    while True:
        message = await topico1_queue.get()
        print(f"Mensaje recibido en el topico 1: {message}")

async def topico2_consumer(): #crea una tarea que escucha el topico 2
    while True:
        message = await topico2_queue.get()
        print(f"Mensaje recibido en el topico 2: {message}")

topico1_queue = asyncio.Queue() 
topico2_queue = asyncio.Queue()
#

async def distributor(client): #distribuye los mensajes a las tareas correspondientes
    async for message in client.messages:
        if message.topic.matches(os.environ['TOPICO1']):
            topico1_queue.put_nowait(message.payload)
        elif message.topic.matches(os.environ['TOPICO2']):
            topico2_queue.put_nowait(message.payload)


async def cont_up(cont): #incrementa el contador cada 3 segundos en una tarea
    logger = logging.getLogger("task-contador")
    while True:
        await asyncio.sleep(3)
        cont['valor'] +=1
        logger.info(f"contador incrementado: {cont['valor']}")

async def pub(cont, cliente): #publica cada 5 segundos el estado del contador en una tarea
    logger = logging.getLogger("task-publicador")
    while True:
        await asyncio.sleep(5)
        logger.info(f"contador publicado: {cont['valor']}")       
        await cliente.publish(os.environ['TOPICOPUB'], str(cont['valor']).encode())
    

async def main():
    tls_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    tls_context.verify_mode = ssl.CERT_REQUIRED
    tls_context.check_hostname = True
    tls_context.load_default_certs()

    cont = {'valor' : 0}

    async with aiomqtt.Client(
        os.environ['SERVIDOR'],
        port=8883,
        tls_context=tls_context,
    ) as client:
        await client.subscribe(os.environ['TOPICO1'])
        await client.subscribe(os.environ['TOPICO2'])
        async with asyncio.TaskGroup() as tg:
            tg.create_task(distributor(client))
            tg.create_task(topico1_consumer())
            tg.create_task(topico2_consumer())
            tg.create_task(cont_up(cont))
            tg.create_task(pub(cont, client))
        await client.wait_for_disconnect()


if __name__ == "__main__":
    try: 
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Cliente MQTT detenido por el usuario.")
    


