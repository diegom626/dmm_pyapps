#!/usr/bin/env python
from sys import stdout
list= ['hola','esto','es','una','prueba','de','loop','en','una','linea']
# print ' '.join([str(i) for i in list])
# print ' '.join(["-a " + str(i) for i in list])
archivos= ['/opt/SUNWappserver/domains/domain1/logs/20170921_Contenedores.11L', '/opt/SUNWappserver/domains/domain1/logs/20170921_Contenedores.10L', '/opt/SUNWappserver/domains/domain1/logs/20170921_Contenedores.16L', '/opt/SUNWappserver/domains/domain1/logs/20170922_Contenedores.09L']

for x in range(len(archivos)):
    archivos.append("-a")
print archivos

