#!/usr/bin/python
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# Name: Conversor - Binario / Decimal
# version: 1.0.0
# Developer: 7H3uz
# Created: 18/03/2021
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

import os, sys, time
from time import sleep as timeout
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
os.system("clear")
print (" ██████╗ ██████╗ ███╗   ██╗██╗   ██╗ ")
print ("██╔════╝██╔═══██╗████╗  ██║██║   ██║ ")
print ("██║     ██║   ██║██╔██╗ ██║██║   ██║ ")
print ("██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝ ")
print ("╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝  ")
print (" ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝   ")
print ("Create By : 7H3uz")
print
print ("           [1]> 1 - Converter Binario em Decimal")
print ("           [2]> 2 - Converter Decimal em Binario")
print 
print (" [0]> Exit ")
print
A = input("Option ==>> ")

if A == "1" or A == "01":
  dec = int(input("Número Binario: "), 2)
  # imprimido o número em decimal
  print(dec)

elif A == "2" or A == "02": 
  # função que comverte decimal para binario
  def binary(numero):
    if numero > 1:
       binary(numero//2)
    print(numero % 2,end = '')
  # lendo um número decimal
  decimal = int(input("Número Decimal: "))
  binary(decimal)
elif A == "0" or A == "00":
    sys.exit() #Aqui é para fechar o arquivo
    
else:
     print ("\nERROR: Wrong Input")
     timeout(3)
     restart_program()