#!/usr/bin/env python
import re
from pprint import pprint

network_devices = {}
with open("files/r1_cdp.txt", "r") as file_a:
    for line in file_a.readlines():
        if "Device ID: " in line:
            hostname = re.findall(r"Device ID: (.+)", line)
        if "Capabilities: " in line:
            capa_1 = re.findall(r"Capabilities: (.+?) ", line)
        z = re.findall(r"Platform: (.+) (.+),", line)
        for x, y in z:
            vendor, model = x, y
network_devices['remote_hostname'] = hostname
network_devices['vendor'] = vendor
network_devices['model'] = model
network_devices['type'] = capa_1
pprint(network_devices)
