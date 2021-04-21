#!/usr/bin/env python


def ip_valid(ip_addr):
    ip_addr = ip_addr.split(".")
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
