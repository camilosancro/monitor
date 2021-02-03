import psutil
import platform
import datetime

"""
Función quie trae el uso de la CPU
"""

# Información del systema

uname = platform.uname()

print("Porcesador: {}".format(uname.processor))
print("Sistema operativo: {}".format(uname.system))
print("Nombre: {}".format(uname.node))
print("Machine: {}".format(uname.machine))
print("Version: {}".format(uname.version))
print("Release: {}".format(uname.release))

#Información de los procesos

for process in psutil.process_iter():
    print(process)

#Información de los usuarios conectados
usuarios = psutil.users()

print(usuarios)



