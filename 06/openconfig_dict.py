#!/usr/local/bin/python3.8

openconfig_interfaces = {
			  "interfaces": {
                            "interface": [
                              {
                                "name": "Ethernet1",
                                "config": {
                                  "name": "Ethernet1",
                                  "type": "ethernetCsmacd",
                                  "mtu": 1514,
                                  "enabled": True
                                }
                              },
                              {
                                "name": "Ethernet2",
                                "config": {
                                  "name": "Ethernet2",
                                  "type": "ethernetCsmacd",
                                  "mtu": 1514,
                                  "enabled": True
                                }
                              }
                            ]
                          }
                        }

print('The whole data model is: {}'.format(openconfig_interfaces))

print('You have the following interfaces: {}'.format(openconfig_interfaces['interfaces']['interface']))

print('One of the interfaces has the following name: {}'.format(openconfig_interfaces['interfaces']['interface'][0]['config']['name']))
