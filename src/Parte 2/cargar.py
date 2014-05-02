#! /usr/bin/python
#!encoding: UTF-8

name = raw_input("Introduzca el nombre del fichero a cargar: ")
f = open(name, "r")
carga = f.readlines()
print "\n"
for i in range(len(carga)):
    print carga[i]
print "\n"
