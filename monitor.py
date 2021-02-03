#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, json, subprocess, psutil, requests, platform, socket

payload={}

def servidor():
    payload['servidor'] = []
    uname = platform.uname()
    cpu_usage = psutil.cpu_percent(interval=2)
 
    payload['servidor'].append({
                    "nombre_servidor": uname.node,
                    "procesador": uname.machine,
                    "sistema_operativo": uname.system,
                    "version": uname.version,
                    "cpu_uso": float(cpu_usage)
            })

def ip_servidor():
    nombre_equipo = socket.gethostname()
    direccion_equipo = socket.gethostbyname(nombre_equipo)
    payload['ip'] = direccion_equipo
    
def usuarios():
        payload['usuarios'] = []
        for usuario in psutil.users():
            payload['usuarios'].append({
                    "nombre_usuario": usuario[0],
                    "pid_usuario": usuario[4],
                    "terminal": usuario[1]
            })

def procesos():
        payload['procesos'] = []
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            payload['procesos'].append({
                "nombre_proceso": proc.info['name'],
                "pid_proceso" : proc.info['pid'],
                "username": proc.info['username']
            })    

def print_json():
    datosaprocesar = json.dumps(payload)
    print(datosaprocesar)

def post_info():
    #URL DE  SERVICIO REST
    url = 'http://54.236.147.177/registrar'
    #url = 'http://127.0.0.1:8080/registrar'

    response = requests.post(url, json=payload)
    print(response)

    if response.status_code == 200:
        print(response.content)

if __name__ == "__main__":
    servidor()
    ip_servidor()
    usuarios()
    procesos()
    print_json()
    post_info()