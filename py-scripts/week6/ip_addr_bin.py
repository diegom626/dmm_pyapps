#!/usr/bin/env python
from func_binary import func_binary
from func_ip import ip_valid


ip_addr_1 = raw_input('\n\nIngrese una direccion IP: ')
if not ip_valid(ip_addr_1):
    print "La ip ingresada no es valida, intente nuevamente"
else:
    to_bin = func_binary(ip_addr_1)
    print "\n%18s     %-40s\n" % (ip_addr_1, to_bin)
