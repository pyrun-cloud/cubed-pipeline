#!/bin/sh
# Iniciar el runtime de Lambda en segundo plano
/usr/local/bin/python -m awslambdaric handler.entry_point.lambda_handler &

# Aquí podrías iniciar otros procesos o ejecutar alguna tarea adicional

# Mantener el contenedor vivo (por ejemplo, esperando en un "tail" infinito)
tail -f /dev/null
