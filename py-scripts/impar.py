#!/usr/bin/env python

num = raw_input('Ingrese numero correspondiente: ')
impar = 1
count = 1
suma = 0

while count <=int(num):
    suma = impar + suma
    count +=  1
    impar +=  2
print "el numero es : %s" % suma
