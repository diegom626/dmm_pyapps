#!/usr/bin/env python
import re

f = open("files/ospf_single_interface.txt", "r")
ospf_data = f.read()
f.close()
data_list = ospf_data.split('\n')
ospf_dic = {}

for line in data_list:
    int_1 = re.search(r"(.+) is up, line protocol is up", line)
    if int_1:
        ospf_dic['Int'] = int_1.group(1)
    ip_addr = re.search(r"Internet Address (.+?), Area (.+),", line)
    if ip_addr:
        ospf_dic['IP'] = ip_addr.group(1)
        ospf_dic['Area'] = ip_addr.group(2)
    type_1 = re.search(r"Network Type (.+?), Cost: (.+)", line)
    if type_1:
        ospf_dic['Type'] = type_1.group(1)
        ospf_dic['Cost'] = type_1.group(2)
    hell_dead = re.search(r"Hello (\d*), Dead (\d*),", line)
    if hell_dead:
        ospf_dic['Hello'] = hell_dead.group(1)
        ospf_dic['Dead'] = hell_dead.group(2)
campos_1 = ['Int', 'IP', 'Area', 'Type', 'Cost', 'Hello', 'Dead']
print
for k in campos_1:
    print "%10s : %-20s" % (k, ospf_dic[k])
