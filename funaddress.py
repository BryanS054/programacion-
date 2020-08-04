# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:45:41 2020
@author: Bryan
"""
def direccion(calle,sector,codigopostal,referencia,numcasa):
    print("su direccion es;","Su sector es:",sector,"calle",calle)
    print("Su casa es la #:",numcasa,"Con codigo postal # :",codigopostal)
    print("y esta cerca de :",referencia)
    
print("Ingrese los datos que se solicita de direccion: ")
c=input("ingrese la calle: ")
s=input("ingrese el sector de residencia: ")
cod=input("Ingrese el codigo postal; ")
r=input("Ingrese una referencia de su domicilio: ")
num=input("ingrese le numero de casa: ")

direccion(c,s,cod,r,num)