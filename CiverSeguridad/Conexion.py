#!/usr/bin/env python
#_*_ coding: utf-8 _*_
#author: Antonio

import requests, os, argparse
os.system("cls")

parser= argparse.ArgumentParser(description= "Detector de cabeceras")
parser.add_argument("-t","--target", help="Objetivo")
parser= parser.parse_args()

def main():
    if parser.target:
        try:
            url= requests.get(url= parser.target)
            cabeceras = dict(url.headers)
            for x in cabeceras:
                print(x + " : " + cabeceras[x])
        except:
            print("No se ha podido conectar")
    else:
        print("No hay objetivo")

if __name__ == "__main__":
    main()
    