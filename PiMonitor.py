#!/usr/bin/python
import subprocess
from subprocess import call
print 'Temperatura:'
subprocess.call(["vcgencmd","measure_temp"])
print 'Uso de Memoria RAM:'
subprocess.call(["free","-m"])
print 'Uso de SD:'
subprocess.call(["df","-Bm"])
print 'Usuarios Activos:'
subprocess.call(["who"])
