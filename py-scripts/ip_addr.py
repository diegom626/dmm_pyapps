ip_addr = raw_input("\n\nIngrese la direccion IP plis: ")

octetos = ip_addr.split(".")
print octetos[:3]
octetos = octetos[:3]
octetos.append('0')
ip_red = ".".join(octetos)

print "\nSu direccion de red es: %s" % ip_red

primer_octet = bin(int(octetos[0]))
octet_hex = hex(int(octetos[0]))
print "%20s %20s %20s" % ("DIRECCION_RED", "1ER_OCTETO_BINARIO", "1ER_OCTETO_HEX")
print "%20s %20s %20s" % (ip_red, primer_octet, octet_hex)
print "\n"

