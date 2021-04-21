#!/usr/bin/env python
import sys
valido = True 
ip_addr = sys.argv.pop()
print sys.argv
split_ip = ip_addr.split(".")
first_octet, second_octet, third_octet, fourth_octet = split_ip
if len(split_ip) == 4:
    if (int(split_ip[0]) >= 1) and (int(split_ip[0]) <= 223) and (int(split_ip[0]) != 127): 
        #evalua si esta en el rango 169.254
        if (first_octet !=169) and (second_octet !=254):
            for i in (second_octet, third_octet, fourth_octet):
                if (int(i) < 0) or (int(i) >= 255):
                    valido = False
    else: valido = False
if valido:
    print "La ip ingresada SI es valida: %s" % ip_addr
else: sys.exit ("\nLa Ip ingresada no es valida: %s" % ip_addr)

