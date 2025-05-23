# Termostato IoT con control por Telegram y MQTT

Este proyecto consiste en un sistema de control de temperatura implementado con una Raspberry Pi Pico W. La configuración permite monitorear y controlar parámetros como el setpoint, modo de funcionamiento, estado del relé, periodo y destello del LED. El control se hace mediante comandos enviados desde un bot de Telegram, y la comunicación se realiza usando MQTTs con TLS.

## Componentes principales

- **Bot de Telegram**: recibe comandos del usuario, valida si está autorizado y publica los datos en los tópicos MQTT correspondientes.
- **Broker MQTT**: se usa Mosquitto con TLS (puerto personalizado), configurado en una VPS.
- **Dispositivo IoT (Raspberry Pi Pico W)**: suscribe a los tópicos y ejecuta las acciones (por ejemplo, activar relé, destello, etc).

## Comandos disponibles en el bot

- `/start` – Inicia la conversación.
- `/acercade` – Info básica del proyecto.
- `/setpoint <valor>` – Define el setpoint de temperatura.
- `/periodo <valor>` – Define el periodo de actualización.
- `/menu` – Muestra un menú con botones para:
  - Cambiar modo (auto/manual)
  - Encender/apagar relé (solo en modo manual)
  - Activar destello del LED

Los comandos con botones envían internamente mensajes de texto que son tratados como comandos válidos.

## Estructura de tópicos MQTT

- `setpoint`
- `periodo`
- `modo` → 0: manual, 1: automático
- `rele` → 0: off, 1: on
- `destello` → mensaje recibido activa una bandera

## Requisitos

- Python 3.11+
- `python-telegram-bot` (v20+)
- `aiomqtt`
- `nest_asyncio` (para correr correctamente en entorno asíncrono)
- Un broker MQTT que soporte TLS

## Notas

- Los usuarios autorizados están definidos en el código.
- El bot se conecta al broker usando TLS con certificados verificados.
- No se almacena el valor de destello, solo se actúa al recibirlo.
