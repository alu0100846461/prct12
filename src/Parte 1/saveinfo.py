#! /usr/bin/python
#!encoding: UTF-8

import info

fname = raw_input("Introduzca el nombre del fichero de salida: ")
fich = open(fname, "w")

hard = info.hardware ()
soft = info.software ()

khard = hard.keys()
ksoft = soft.keys()

fich.write("    ---- HARDWARE INFORMATION ----" + "\n\n")
for key in khard:
    fich.write (key + ": " + hard[key] + "\n")
fich.write("\n" + "    ---- SOFTWARE INFORMATION ----" + "\n\n")

for key in ksoft:
    fich.write (key + ": " + soft[key] + "\n")

fich.close()
