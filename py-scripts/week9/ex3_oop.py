#!/usr/bin/env python
from ex1_oop import IpAddress


class IpAddressWithNetmask(IpAddress):

    def __init__(self, ip_addr):
        (ip_addr, netmask) = ip_addr.split('/')
        self.netmask = '/' + netmask
        IpAddress.__init__(self, ip_addr)

    def netmask_in_dotdecimal(self):
        cidr_mask = int(self.netmask.strip('/'))
        if cidr_mask > 32:
            return False
        zero_string = '0' * (32 - cidr_mask)
        one_str = '1' * cidr_mask
        full_str = one_str + zero_string
        (octeto_1, octeto_2, octeto_3, octeto_4) = full_str[:8], full_str[8:16], full_str[16:24], full_str[24:]
        cidr = ['0', '0', '0', '0']
        for i, octet in enumerate((octeto_1, octeto_2, octeto_3, octeto_4)):
            cidr[i] = str(int(octet, 2))
        return '.'.join(cidr)

    def network_range(self):
        # Mascara en formato prefijo
        cidr_mask = int(self.netmask.strip('/'))
        binary__ = self.convert_to_binary().replace('.', '')
        # Asignar valor binario de id de red y divide string en octetos
        binary_net_id = binary__[:cidr_mask] + '0' * (32 - cidr_mask)
        (octeto_1, octeto_2, octeto_3, octeto_4) = binary_net_id[:8], binary_net_id[8:16], binary_net_id[16:24], \
                                                   binary_net_id[24:]
        # Asignar valor binario de broadcast de red y divide strings en octetos
        binary_net_broad = binary__[:cidr_mask] + '1' * (32 - cidr_mask)
        (broad_1, broad_2, broad_3, broad_4) = binary_net_broad[:8], binary_net_broad[8:16], binary_net_broad[16:24], \
                                                   binary_net_broad[24:]
        # Convierte de binario a decimal correspondiente
        network_id = [octeto_1, octeto_2, octeto_3, octeto_4]
        network_broad = [broad_1, broad_2, broad_3, broad_4]
        range_net = {}
        for i, octet in enumerate(network_id):
            network_id[i] = str(int(octet, 2))
        for i, octet in enumerate(network_broad):
            network_broad[i] = str(int(octet, 2))
        # Calculamos el valor del primer host valido y el ultimo
        network_id[3] = str(int(network_id[3]) + 1)
        network_broad[3] = str(int(network_broad[3]) - 1)
        range_net['HostMin'] = '.'.join(network_id)
        range_net['HostMax'] = '.'.join(network_broad)
        return range_net['HostMin'], range_net['HostMax']

def main():
    '''
    Basic test on code
    '''
    addr_1 = IpAddressWithNetmask('192.1.200.25/26')
    print
    print "%15s: %-40s" % ("IP", addr_1.ip)
    print "%15s: %-40s" % ("Netmask", addr_1.netmask)
    print "%15s: %-40s" % ("Binary IP", addr_1.convert_to_binary())
    print "%15s: %-40s" % ("Hex IP", addr_1.display_in_hex())
    print "%15s: %-40s" % ("IP Valid", addr_1.is_valid())
    print "%15s: %-40s" % ("Netmask dot dec", addr_1.netmask_in_dotdecimal())
    print "%15s: %-40s" % ("Network range", addr_1.network_range())
    print


if __name__ == "__main__":
    main()


