#! /usr/bin/python
#!encoding: UTF-8

import sys
import time

# Función destinada a calcular el valor aproximado del número pi.
def aprox (n):
    suma = 0.0
    for i in range (1, int(n+1)):
        xi = (i-0.5)/n
        fxi = 4/(1+xi**2)
        suma += fxi
    pi = suma/n 
    return pi

# Función destinada a la detección de errores.
def error (n, t, umbral):
    sol = 0.0
    warn = 0.0
    ref = aprox(n)
    for j in range (t):
        pi = aprox(n)
        if (abs(pi - ref) > umbral):
            warn += 1
    return (warn/t) * 100

# Función destinada a almacenar los resultados del experimento en un fichero.
def save (name, intervalos, umbrales):
    num_iter = 10   # Número de comprobaciones en cada llamada a la función "error".
    t0 = time.time()   # Referencia para medir el tiempo total de ejecución
    c0 = time.clock()  # Referencia para medir el tiempo de uso de CPU
    f = open(name, "w")
    f.write("    ---- RESULTADOS DEL EXPERIMENTO ----" + "\n")
    for i in range (len(intervalos)):
        f.write("\n" + "Valor real: " + str(PI) + ", ")
        f.write("Intervalos: " + str(intervalos[i]) + ", ")
        pi = aprox(intervalos[i])
        f.write("Valor obtenido: " + str(pi) + ", ")
        for j in range (len(umbrales)):
            sol = error(intervalos[i], num_iter, umbrales[j])
            if j < (len(umbrales) - 1):
                f.write(str(sol) + "% (umbral " + str(umbrales[j]) + "), ")
            else:
                f.write(str(sol) + "% (umbral " + str(umbrales[j]) + ")")
    tf = time.time() - t0
    cf = time.clock() - c0
    f.write("\n\n" + "Tiempo total de ejecución: " + str(tf) + " segundos")
    f.write("\n" + "Tiempo de uso de CPU: " + str(cf) + " segundos")
    f.close()

PI = 3.1415926535897931159979634685441852
intervalos = (1e1, 1e2, 1e3, 1e4, 1e5, 1e6)
umbrales = (1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6)
fname = raw_input("Nombre deseado para el fichero de salida: ")
save(fname, intervalos, umbrales)



