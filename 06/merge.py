#!/usr/local/bin/python3.8

ip = {
       'address': '192.168.100.1',
       'prefix': 24
     }

phy = {
        'name': 'Ethernet1',
        'speed': 10000,
        'mtu': 1514,
        'enabled': True,
        'description': 'Test Interface'
      }

interface = {**ip, **phy}

print('The interface data is: {}'.format(interface))
