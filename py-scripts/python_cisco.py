#!/usr/bin/env python
cisco = 'Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)'

cisco_split = cisco.split(",")
cisco_version = cisco_split[2] 
number = cisco_version.split()
number2 = number[1]

print number2

