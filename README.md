# Cliente MQTT Asíncrono con TLS

Este proyecto es una aplicación en Python que se conecta a un broker MQTT usando comunicación cifrada (MQTTS). Se ejecuta dentro de un contenedor Docker y utiliza `aiomqtt`.

## Características

- Se conecta a un broker usando MQTT sobre TLS.
- Se suscribe a dos tópicos definidos por variables de entorno.
- Cada tópico tiene su propia corrutina que procesa los mensajes.
- Publica el valor de un contador cada 5 segundos en otro tópico.
- El contador se incrementa cada 3 segundos en una tarea separada.
- Usa logging con el nombre de la tarea.
- Captura la interrupción por `Ctrl+C` para cerrar correctamente.
- Configuración mediante archivo `.env`.

