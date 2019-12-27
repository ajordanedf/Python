#!/usr/bin/env python
#_*_ coding: utf8 _*_
#Author: Toni


# archivo= open("./ArchivosCreadosPorPython/Archivo1.txt", "w")
# nombre= input("Nombre: ")
# Apellidos= input("Apellidos: ")
# Edad= input("Edad: ")
# Pais= input("Pais: ")

# archivo.write("\n" + nombre + "\n")
# archivo.write(Apellidos + "\n")
# archivo.write(Edad + "\n")
# archivo.write(Pais + "\n")

# print("Pos oiga señora, esto funciona")

# archivo.close()

# archivo= open("./ArchivosCreadosPorPython/Archivo1.txt", "r")

# for l in archivo.read().split("\n"):
#     print(l)

# print("Pos oiga señora, esto funciona")

# archivo.close()


archivo= open("./ArchivosCreadosPorPython/Archivo1.txt", "a")

archivo.write(input("\nDedicacion: "))
archivo.write(input("\nEstatura: "))

archivo.close()
