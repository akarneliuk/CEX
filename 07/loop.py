#!/usr/local/bin/python3.8

interfaces = [{'name': 'Ethernet1'}, {'name': 'Ethernet2'}, {'name': 'Ethernet3'}]

print('The list of the interfaces:')

for interface in interfaces:
    print('Your interfaces is {}'.format(interface))
    print('More precisely {}'.format(interface['name']))


interfaces2 = {
                'Ethernet1': {
                               'speed': 10000,
                               'enabled': True
                             },
                'Ethernet2': {
                               'speed': 10000,
                               'enabled': True
                             },
                'Ethernet3': {
                               'speed': 10000,
                               'enabled': True
                             }
              }

print('The dictionary of the interfaces:')

for interface_key, interface_value in interfaces2.items():
    print('Internface {} has {} speed and it is {}ly enabled'.format(interface_key, interface_value['speed'], interface_value['enabled']))
