#! /usr/bin/env python
# -*- coding: utf-8 -*-

#DNI Tool in python
#Pequeño script para generar la letra de un DNI

def ra():
#Variable numero para definir lo que introdusca el usuario
    numero = raw_input("Dame los numeros del DNI: ")

    intnumero = int(numero)
#Variable letra1 que contiene las letras del DNI
    letra1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    resto = intnumero%23

    letra = letra1[resto]

    print ("La letra del DNI es:",letra,"Y su numero completo: ",numero, letra)

ra()
