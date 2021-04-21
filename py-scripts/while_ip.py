#!/usr/bin/env python
IP = False
while not IP:
    prompt_ip = raw_input("Favor ingrese una direccion IP: ")
    valido = True
    ip_addr = prompt_ip.split(".")
    if len(ip_addr) != 4:
        continue
    for i, octeto in enumerate(ip_addr):
        try:
            ip_addr[i] = int(octeto)
        except ValueError:
            # couldn't convert octet to an integer
            print "\n\nIP Debe ser un numero: %s\n" % octeto
            valido = False
    if not valido:
        continue
    octeto_1, octeto_2, octeto_3, octeto_4 = ip_addr
    if octeto_1 < 1:
        valido = False
    elif octeto_1 > 223:
        valido = False
    elif octeto_1 == 127:
        valido = False
        print '1er octeto no debe ser rango privado'
    if octeto_1 == 169 and octeto_2 == 254:
        valido = False
        print 'Ingrese un rango valido'
    for x in (octeto_2, octeto_3, octeto_4):
        if x < 0 or x > 255:
            valido = False
    if valido:
        IP = True
    else:
        print 'Favor intente nuevamente'
print 'IP CORRECTA'
