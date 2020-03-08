#!/usr/local/bin/python3.8

ip = {
       'address': '192.168.100.1',
       'prefix': 24
     }

print('Your dictionary is {}'.format(ip))
print('The device IP is {}'.format(ip['address']))

ip['family'] = 'ipv4'

print('Your dictionary is {}'.format(ip))

del ip['prefix']

print('Your dictionary is {}'.format(ip))

ip.update({'type': 'primary'})

print('Your dictionary is {}'.format(ip))

address = ip.pop('address', None)

print('Your dictionary is {} and removed element is {}'.format(ip, address))

address = ip.pop('address', None)

print('Your dictionary is {} and removed element is {}'.format(ip, address))

