#!/usr/bin/env python
import sys
sys.path.append('../week6')
from func_ip import ip_valid

if __name__ == '__main__':
    test_ip_addresses = {
        '192.168.1': False,
        '10.1.1.': False,
        '10.1.1.x': False,
        '0.77.22.19': False,
        '-1.88.99.17': False,
        '241.17.17.9': False,
        '127.0.0.1': False,
        '169.254.1.9': False,
        '192.256.7.7': False,
        '192.168.-1.7': False,
        '10.1.1.256': False,
        '1.1.1.1': True,
        '223.255.255.255': True,
        '223.0.0.0': True,
        '10.200.255.1': True,
        '192.168.17.1': True,
    }
    for k, v in test_ip_addresses.items():
        if v is ip_valid(k):
            dots_to_print = (25 - len(k)) * '.'
            if ip_valid(k):
                print '%s %s: correcto' % (k, dots_to_print)
            else:
                print '%s %s: incorrecto' % (k, dots_to_print)
