#!/usr/bin/env python
import re
f = open("./files/ospf_data.txt", "r")
ospf_datos = f.read()
f.close()

search = re.split(r"(.+ is up, line protocol is up)", ospf_datos)

def separate_interface_data(ospf_data):
    """
    Take 'show ip ospf interface' data as a string
    Return a list corresponding to each section of the data
    (where a section pertains to one interface)
    ['interface1 ospf info', 'interface2 ospf info', etc ]
    """

    # Split the data based on 'is up, line protocol is up' but retain this string
    ospf_data = re.split(r'(.+ is up, line protocol is up)', ospf_data)
    # Dump any data before the first 'is up, line protocol is up'
    ospf_data.pop(0)
    # print ospf_data
    ospf_list = []
    while True:
        if len(ospf_data) >= 2:
            intf = ospf_data.pop(0)
            section = ospf_data.pop(0)
            # reunify because it was split up in the re.split
            ospf_string = intf + section
            ospf_list.append(ospf_string)
        else:
            break
    return ospf_list
print separate_interface_data(ospf_datos)
