#!/bin/bash
watch -n 2 "echo Temperatura: && vcgencmd measure_temp && echo Uso de RAM: && free -m && echo Usuarios: && who"
