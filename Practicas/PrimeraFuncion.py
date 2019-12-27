#!/usr/bin/env python
#_*_ coding: utf8 _*_

#Main es la función principal por que se lo decimos en el if
#__name__ es una mierda de estas que ya tiene el python predefinido.

import os

def main():
    os.system("cls")
    print("Main ejecutado\n")
    saludo()
    despedida()
    
    
def saludo():
    print("Hola buenos dias :D")
    
def despedida():
    print("Aleh a tomnar por culo")

if __name__ == "__main__":
    main()

    