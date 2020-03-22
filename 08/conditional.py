#!/usr/local/bin/python3.8

interfaces = [
               {'name': 'Ethernet1', 'enabled': True, 'ipv4': '192.168.100.1/24'},
               {'name': 'Ethernet2', 'enabled': False, 'vlan': 'tagged'},
               {'name': 'Ethernet3', 'enabled': True, 'ipv4': '192.168.101.1/24', 'vlan': 'tagged'}
             ]

config_lines = []

for iface_entry in interfaces:
    config_lines.append('interface {}'.format(iface_entry['name']))

    if iface_entry['enabled']:
        config_lines.append('  no shutdown')

    else:
        config_lines.append('  shutdown')

    if ('ipv4' in iface_entry or 'ipv6' in iface_entry) and 'vlan' not in iface_entry:
        config_lines.append('  no switchport')

        if 'ipv4' in iface_entry:
           config_lines.append('  ipv4 address {}'.format(iface_entry['ipv4']))

        if 'ipv6' in iface_entry:
           config_lines.append('  ipv6 address {}'.format(iface_entry['ipv6']))

    elif 'vlan' in iface_entry and not ('ipv4' in iface_entry or 'ipv6' in iface_entry):
        config_lines.append('  switchport')

        if iface_entry['vlan'] == 'tagged':
           config_lines.append('  switchport mode trunk')

        elif iface_entry['vlan'] == 'untagged':
           config_lines.append('  switchport mode access')    

    else:
        config_lines.pop(-1)
        config_lines.append('  descriontion THERE IS SOME MESS WITH VARS')
        config_lines.append('  shutdown')

    config_lines.append('!')

for line in config_lines:
    print(line)
