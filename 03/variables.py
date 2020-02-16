#!/usr/local/bin/python3.8

port_name = 'Ethernet1'
port_ip_address = '192.168.100.1'
port_speed = 10000
port_ip_prefix = 24
port_enabled = True
port_switch = False

print('Interface {} has an IP address {}/{}'.format(port_name, port_ip_address, port_ip_prefix))

port_ip = '{}/{}'.format(port_ip_address, port_ip_prefix)

print(port_ip)
