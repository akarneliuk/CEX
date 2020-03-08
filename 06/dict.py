#!/usr/local/bin/python3.8

ip = {
       'ip': '192.168.100.1',
       'prefix': 24
     }

print('The dict is {}'.format(ip))
print('IP is {}'.format(ip['ip']))

ip['family'] = 'ipv4'

print('The dict is {}'.format(ip))

ip.update({'primary': True})

print('The dict is {}'.format(ip))

del ip['family']

print('The dict is {}'.format(ip))

deleted_value = ip.pop('primary', None)

print('The dict is {}, deleted {}'.format(ip, deleted_value))

deleted_value = ip.pop('primary', None)

print('The dict is {}, deleted {}'.format(ip, deleted_value))

