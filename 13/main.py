#!/usr/local/bin/python3.8

# Modules
import sys
from bin.ip_converter import get_ip_list

# Variables
if len(sys.argv) < 3:
    target_ips = '10.0.0.3-10.0.1.15'

else:
    target_ips = f'{sys.argv[1]}-{sys.argv[2]}'

ip_list = get_ip_list(target_ips)

print(f'Your IPs are: ')
for ip in ip_list:
    print(ip)