#!/usr/local/bin/python3.8

input_string = 'PE1-BLN-DE,Equinix FR5,10.0.0.11/24,,Cisco NCS 5500'

dev_params = input_string.split(',')

print('The parsed values are {}'.format(dev_params))

ip_addr, ip_prefix = dev_params[2].split('/')

print('The IP is {} with the prefix {}'.format(ip_addr, ip_prefix))

final_string = ','.join(dev_params)

print('The final string is {}'.format(final_string))

ip_addr_pref = '/'.join([ip_addr, ip_prefix])

print('The IP and prefix is {}'.format(ip_addr_pref))
