#!/usr/local/bin/python3.8

# Variables
ip_addresses = '10.0.0.3-10.0.1.15'


# User-defined functions
def ip_int_str(operation, input_var):
    if operation == 'get_int':
        list_addr = input_var.split('.')
        temp_number = 0
        index = len(list_addr) - 1

        while index >=0:
            temp_number += (int(list_addr[index]) * (256 ** (len(list_addr) - 1 - index)))
            index -= 1

    elif operation == 'get_str':
        decr = input_var
        index = 0
        temp_number = []

        while decr > 0:
            temp_number.append(str(int(decr / 256 ** (3 - index))))
            decr %= (256 ** (3 - index))
            index += 1

        temp_number = '.'.join(temp_number)

    return temp_number


# Main body
ip_start, ip_end = ip_addresses.split('-')

num_ip_s = ip_int_str('get_int', ip_start)
num_ip_e = ip_int_str('get_int', ip_end)

if num_ip_s <= num_ip_e:
    num_ip_t = num_ip_s

    print('Printing IP in range {}'.format(ip_addresses))

    while num_ip_t <= num_ip_e:
        ip_addr = ip_int_str('get_str', num_ip_t)
        print('IP is {}'.format(ip_addr))

        num_ip_t += 1

else:
    print('The starting IP in the range is higher than the final one.')

