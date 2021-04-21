#!/usr/bin/env python
show_ver = '''
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support:
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command

Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)

License Info:
License UDI:
-------------------------------------------------
Device#   PID                   SN
-------------------------------------------------
*0        CISCO881-SEC-K9       FTX1000038X

License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices

Configuration register is 0x2102
'''
show_ver = show_ver.split("\n")
dict_cisco = {}

for line in show_ver:
    #Verificar Fabricante
    if 'Cisco IOS Software' in line:
        dict_cisco['Vendor'] = 'Cisco Systems'
    #Version
        OS_VERSION = line.split(',')[2]
        dict_cisco['Version'] = OS_VERSION.split()[1]
    #Modelo
        dict_cisco['model'] = line.split()[3]
    #UPTIME
    if 'uptime' in line:
        uptime = line.split('uptime is ')[1]
        dict_cisco['uptime'] = uptime
    #SN
    if 'Processor board ID' in line:
        dict_cisco['serial'] = line.split()[3]
print '%-15s %-15s %-15s %-40s %-15s' % ('Fabricante', 'Version', 'Modelo', 'Uptime', 'Serial')
print '%-15s %-15s %-15s %-40s %-15s' % (dict_cisco['Vendor'], dict_cisco['Version'], dict_cisco['model'], dict_cisco['uptime'], dict_cisco['serial'])

    
