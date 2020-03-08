#!/usr/local/bin/python3.8

ip = {
       'ip': '192.168.100.1',
       'prefix': 24
     }

phy = {
        'speed': 10000,
        'mtu': 1514,
        'enabled': True
      }

interface = {**ip, **phy}

print(interface)
