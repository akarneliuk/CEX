#!/usr/local/bin/python3.8

interfaces = [{'name': 'Ethernet1'}, {'name': 'Ethernet2'}]

for interface_entry in interfaces:
    print('Your element is {}'.format(interface_entry))
    print('The key name from element is {}'.format(interface_entry['name']))


interfaces2 = {
                'Ethernet1': {
                  'speed': 10000,
                  'enabled': True
                },
                'Ethernet2': {
                  'speed': 10000,
                  'enabled': True
                }
              }

print('original dict {}'.format(interfaces2))
print('transformed dict {}'.format(interfaces2.items()))

for int_key, int_value in interfaces2.items():
    print('The key is {} and the value is {}'.format(int_key, int_value))
