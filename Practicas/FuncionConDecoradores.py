#!/usr/bin/env python
#_*_ coding: utf8 _*_
#Author: Toni

import os

class Prueba1(object):
    def __init__(self):
        saludo()
    
    #@ClassMethod hace que exista una funcion dentro del objeto y desvinculada del __init__, podemos invocarla con parámetros distintos, solo que hay que pasarle
    #el argumento "cls"
    @classmethod
    def saludo(cls,nombre):
        print("Hola {}".format(nombre))
    
    @staticmethod
    def despedida():
        print("Hasta luego")

def main():
    Prueba1.saludo("Toni")
    
if __name__ == "__main__":
    os.system("cls")
    main()
    