#!/usr/bin/env python
#_*_ coding: utf-8 _*_
#author: Antonio

import mechanize, argparse, os
#Embellecedor
from bs4 import BeautifulSoup

os.system("cls")

parse= argparse.ArgumentParser()
parse.add_argument("-b", "--buscar", help="Opcion a buscar")
parse= parse.parse_args()

def main():
    if parse.buscar:
        bus= mechanize.Browser()
        bus.set_handle_robots(False)
        bus.set_handle_equiv(False)
        bus.addheaders= [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")]
        bus.open("https://www.google.es")
        
        #Recoge el primer formulario, en este caso solo hay uno, pero por si acaso
        bus.select_form(nr=0)
        #Buscamos "q" ya que en el formulario es un TextControll == Entrada de texto
        bus["q"]= parse.buscar
        bus.submit()
        p = BeautifulSoup(bus.response().read(), "html5lib")
        for link in p.find_all("a"):
            u= link.get("href")
            u= str(u).replace("/url?q=", "")
            print(u)
        
        #Para mirar los campos
        # for n in bus.forms():
        #     print(n)
                
    else:
        print("Palabr a buscar")


if __name__ == "__main__":
    main()
    
