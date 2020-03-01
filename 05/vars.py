#!/usr/local/bin/python3.8

initial_string = 'pe1-fra-de,Equinix FR5,10.11.12.13/24,,Cisco NCS 5500'

dev_params = initial_string.split(',')

print('The variables is split into: {}'.format(dev_params))

ip_addr, ip_prefix = dev_params[2].split('/')

print('The IP address is {} with the prefix {}'.format(ip_addr, ip_prefix))

final_string = ','.join(dev_params)

print('The string joined back: {}'.format(final_string))


ip_addr_pref = '/'.join([ip_addr, ip_prefix])

print('The IP address and prefix together is {}'.format(ip_addr_pref))

