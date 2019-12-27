#!/usr/bin/env python
#_*_ coding: utf-8 _*_
#author: Antonio

import requests, os, argparse
os.system("cls")

#Requests --> Sirve para conectarse a sitios web
#Argparse --> Sirve para crear una consola que entienda los parametros que le vamos pasando

#Instancia parser y le decimos para que va a ser el programa
parser= argparse.ArgumentParser(description= "Detector de cabeceras")
#Añadimos un comando, -t o --target(extendido) creará el método .target PERO SON COMANDOS PERSONALIZADOS
parser.add_argument("-t","--target", help="Objetivo")
parser= parser.parse_args()

def main():
    if parser.target:
        try:
            #requests.get --> nos da toda la info de la response solo nos falan métodos
            url= requests.get(url= parser.target)
            cabeceras = dict(url.headers)
            for x in cabeceras:
                #Para recorrer el diccionario
                print(x + " : " + cabeceras[x])
        except:
            print("No se ha podido conectar")
    else:
        print("No hay objetivo")

if __name__ == "__main__":
    main()
    