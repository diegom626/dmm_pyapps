#!/usr/bin/env python


def func_binary(ip_addr):
    octetos = ip_addr.split(".")
    list1 = []
    if len(octetos) == 4:
        for octeto in octetos:
            try:
                if int(octeto) < 0 or int(octeto) > 255:
                    return False
                bin_octeto = bin(int(octeto))
                # quita el 0b del resultado
                bin_octeto = bin_octeto[2:]
                # agregar 0's hasta completar los 8 bits
                while True:
                    if len(bin_octeto) >= 8:
                        break
                    bin_octeto = '0' + bin_octeto
                # anade el resultado a la lista (list1)
                list1.append(bin_octeto)
            except ValueError:
                return False
        list1 = '.'.join(list1)
        return list1
    else:
        return False
print func_binary('192.1.200.1')