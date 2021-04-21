#!/usr/bin/env python
import pprint
import sys
sw1_show_cdp_neighbors = '''
SW1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                                 S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone
Device ID            Local Intrfce        Holdtme        Capability        Platform    Port ID
R1                    Fas 0/11              153            R S I           881          Fas 1
R2                    Fas 0/12              123            R S I           881          Fas 1
R3                    Fas 0/13              129            R S I           881          Fas 1
R4                    Fas 0/14              173            R S I           881          Fas 1
R5                    Fas 0/15              144            R S I           881          Fas 1
'''

sw1_show_cdp_neighbors_detail = '''
SW1> show cdp neighbors detail
--------------------------
Device ID: R1
Entry address(es):
   IP address: 10.1.1.1
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/11, Port ID (outgoing port): FastEthernet1
Holdtime: 153 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
--------------------------
Device ID: R2
Entry address(es):
   IP address: 10.1.1.2
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/12, Port ID (outgoing port): FastEthernet1
Holdtime: 123 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
--------------------------
Device ID: R3
Entry address(es):
   IP address: 10.1.1.3
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/13, Port ID (outgoing port): FastEthernet1
Holdtime: 129 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
--------------------------
Device ID: R4
Entry address(es):
   IP address: 10.1.1.4
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/14, Port ID (outgoing port): FastEthernet1
Holdtime: 173 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
--------------------------
Device ID: R5
Entry address(es):
   IP address: 10.1.1.5
Platform: Cisco 881, Capabilities: Router Switch IGMP
Interface: FastEthernet0/15, Port ID (outgoing port): FastEthernet1
Holdtime: 144 sec
Version :
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
advertisement version: 2
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
'''

r1_show_cdp_neighbors = '''
R1>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/11
'''

r1_show_cdp_neighbors_detail = '''
R1>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/11
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''

r2_show_cdp_neighbors = '''
R2>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/12
'''

r2_show_cdp_neighbors_detail = '''
R2>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/12
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''

r3_show_cdp_neighbors = '''
R3>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/13
'''

r3_show_cdp_neighbors_detail = '''
R3>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/13
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''

r4_show_cdp_neighbors = '''
R4>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/14
'''

r4_show_cdp_neighbors_detail = '''
R4>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/14
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''

r5_show_cdp_neighbors = '''
R5>show cdp neighbors 
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Fas 1              150          S I      WS-C2950- Fas 0/15
'''

r5_show_cdp_neighbors_detail = '''
R5>show cdp neighbors detail 
-------------------------
Device ID: SW1
Entry address(es): 
  IP address: 10.1.1.22
Platform: cisco WS-C2950-24,  Capabilities: Switch IGMP 
Interface: FastEthernet1,  Port ID (outgoing port): FastEthernet0/15
Holdtime : 145 sec
Version :
Cisco Internetwork Operating System Software 
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA8a, RELEASE SOFTWARE (fc1)
Copyright (c) 1986-2006 by cisco Systems, Inc.
Compiled Fri 28-Jul-06 15:16 by weiliu
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000019E845CE80FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
'''
cdp_neighbors = (
    sw1_show_cdp_neighbors_detail,
    r1_show_cdp_neighbors_detail,
    r2_show_cdp_neighbors_detail,
    r3_show_cdp_neighbors_detail,
    r4_show_cdp_neighbors_detail,
    r5_show_cdp_neighbors_detail
)
network_devices = {}
for var in cdp_neighbors:
    cdp_fields = var.split("\n")
    # declaramos las variables de los host
    remote_hostname = ''
    local_hostname = ''
    for dispo in cdp_fields:
        if '----------------' in dispo:
            remote_hostname = ''
        if 'show cdp neighbors detail' in dispo:
            local_hostname = dispo.split('show cdp neighbors detail')[0]
            if '>' in local_hostname:
                local_hostname = local_hostname.split('>')[0]
            elif '#' in local_hostname:
                local_hostname = local_hostname.split('#')[0]
            #else:
            #    sys.exit("Invalid prompt for local hostname - exiting")
            if not local_hostname in network_devices:
                network_devices[local_hostname] = {}
        if 'Device ID' in dispo:
            (junk, remote_hostname) = dispo.split("Device ID: ")
            remote_hostname = remote_hostname.strip()
            # When you find a new device, initialize it as a blank dictionary
            if not remote_hostname in network_devices:
                network_devices[remote_hostname] = {}

            if (local_hostname in network_devices) and remote_hostname:
                if not 'adjacent_dev' in network_devices[local_hostname]:
                    network_devices[local_hostname]['adjacent_dev'] = [remote_hostname]
                else:
                    network_devices[local_hostname]['adjacent_dev'].append(remote_hostname)
        if 'IP address: ' in dispo:
            (junk, ip) = dispo.split("IP address: ")
            ip = ip.strip()
            if remote_hostname:
                network_devices[remote_hostname]['IP'] = ip
        if 'Platform:' in dispo:
            (vendor, model) = dispo.split(",")[0].split("Platform:")[1].split()
            if remote_hostname:
                network_devices[remote_hostname]['vendor'] = vendor
                network_devices[remote_hostname]['model'] = model
        if 'Router' in dispo:
            if remote_hostname:
                network_devices[remote_hostname]['device_type'] = 'router'
        elif 'Switch' in dispo:
            if remote_hostname:
                network_devices[remote_hostname]['device_type'] = 'switch'
print '\n'
pprint.pprint(network_devices)
print '\n'
