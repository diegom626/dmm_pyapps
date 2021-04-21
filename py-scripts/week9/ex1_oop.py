#!/usr/bin/env python


class IpAddress(object):
    def __init__(self, ip):
        self.ip = ip
    def convert_to_binary(self):
        addr_obj = self.ip.split('.')
        list1 = []
        if len(addr_obj) == 4:
            for octeto in addr_obj:
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

    def display_in_hex(self):
        addr_obj = self.ip.split('.')
        list1 = []
        if len(addr_obj) == 4:
            for octeto in addr_obj:
                try:
                    if int(octeto) < 0 or int(octeto) > 255:
                        return False
                    hex_octeto = hex(int(octeto))
                    if len(hex_octeto) > 2:
                        hex_octeto = hex_octeto[2:]
                    # agregar 0's en caso ser un numero entero
                    if len(hex_octeto) == 1:
                        hex_octeto = '0' + hex_octeto
                    list1.append(hex_octeto)
                except ValueError:
                    return False
            list1 = '.'.join(list1)
            return list1
    def is_valid(self):
        ip_addr = self.ip.split(".")
        if len(ip_addr) != 4:
            return False
        try:
            for i, octeto in enumerate(ip_addr):
                ip_addr[i] = int(octeto)
        except ValueError:
            return False
        octet_1, octet_2, octet_3, octet_4 = ip_addr
        if octet_1 <= 0:
            return False
        elif octet_1 == 127:
            return False
        elif octet_1 > 223:
            return False
        if octet_1 == 169 and octet_2 == 254:
            return False
        for x in (octet_2, octet_3, octet_4):
            if x < 0 or x > 255:
                return False
        return True
