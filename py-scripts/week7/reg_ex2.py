#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from pprint import pprint
f = open("files/sw1_cdp.txt", "r")
file = f.read()
f.close()
dict = {}
dict['remote_host'] = re.findall(r"Device ID: (.+)", file)
dict['IPs'] = re.findall(r"IP address: (.+)", file)
dict['platform'] = re.findall(r"Platform: (.+),", file)

# Print output
field_order = ('remote_host', 'IPs', 'platform')
for k in field_order:
    print ("%15s: %-20s" % (k, dict[k]))

