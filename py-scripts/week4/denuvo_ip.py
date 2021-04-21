#!/usr/bin/env python
IP = False
while not IP:
    prompt_ip = raw_input("Favor ingrese una direccion IP: ")
    valido = True
    ip_addr = prompt_ip.split(".")
    if len(ip_addr) !=4:
        valido = False
    try:
        for i, octeto in enumerate(ip_addr):
            ip_addr[i] = int(octeto)
    except ValueError:
        print 'No es un caracter valido para validar %s\n' % octeto
        continue
    octet_1, octet_2, octet_3, octet_4 = ip_addr
    if octet_1 <= 0:
        valido = False
    elif octet_1 == 127:
        print 'No debe ser una ip local'
        valido = False
    elif octet_1 > 223:
        valido = False
    if octet_1 == 169 and octet_2 == 254:
        print 'Debe ser un rango valido'
        valido = False
    
    if valido == False:
        continue
    for x in (octet_2, octet_3, octet_4):
        if x < 0 or x > 255:
            valido = False
    if valido:
        IP = True
print "Lo lograste"

