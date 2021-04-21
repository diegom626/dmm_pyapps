#!/usr/bin/env python

ip_addr = raw_input("\nIngrese una direccion IP: ")
octet_split = ip_addr.split(".")

print "%-15s %-15s %-15s %-15s" % ("1ER_OCTETO", "2DO_OCTETO", "3ER_OCTETO", "4TO_OCTETO")
print "%-15s %-15s %-15s %-15s" % (bin(int(octet_split[0])), bin(int(octet_split[1])), bin(int(octet_split[2])), bin(int(octet_split[3])))
