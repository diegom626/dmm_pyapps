#!/usr/bin/env python
import sys

ip_addr = sys.argv.pop() 
octetos = ip_addr.split(".")
list1 = []
if len(octetos) == 4:
    for octeto in octetos:
        bin_octeto = bin(int(octeto))
        print bin_octeto
        #stripea el 0b de la wea de string
        bin_octeto = bin_octeto[2:] 
        
        # el compadre agregara 0's hasta completar los 8 bits
        while True:
            if len(bin_octeto) >=8:
                break
            bin_octeto = '0' + bin_octeto
        # anade el resultado a la lista (list1)
        list1.append(bin_octeto)
        
    #une los bits en formato ip binario
    list1 = ".".join(list1)
    # imprime la salida
    print "\n%-15s %-45s" % ("DIRECCION IP", "BINARIO")
    print "%-15s %-45s\n\n" % (ip_addr, list1)


else:
    sys.exit("Ip invalida")
