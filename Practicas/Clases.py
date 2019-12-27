#!/usr/bin/env python
#_*_ coding: utf8 _*_
#Author: Toni
import os

class Coche(object):
    def __init__(self):
        self.modelo= "Mini"
        self.color= "Blanco"
        self.ventanas= 4
        self.tipo= "Todo terreno"
    
def main():
    os.system("cls")
    miCoche= Coche()
    print("Mi coche es un {} con {} puertas, creo que es un {}".format(miCoche.modelo, miCoche.ventanas, miCoche.tipo))
    
if __name__ == "__main__":
    main()
