#! /usr/bin/python
#!encoding: UTF-8

import mod_pi

intervalos = (1e1, 1e2, 1e3, 1e4, 1e5, 1e6)
umbrales = (1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6)
fname = raw_input("Nombre deseado para el fichero de salida: ")
mod_pi.save(fname, intervalos, umbrales)
print "\n", "El experimento ha sido realizado satisfactoriamente."
print "Acceda al fichero \"", fname,"\" para consultar los resultados.", "\n"
