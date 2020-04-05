#!/usr/local/bin/python3.8

# Variables
ip_addresses = '10.0.0.3-10.0.1.15'

# User-defined function
def ip_str_int(input_var, operation):
    if operation == 'get_int':
        input_var = input_var.split('.')
        index = len(input_var) - 1
        temp_value = 0

        while index >= 0:
            temp_value += (int(input_var[index]) * (256 ** (len(input_var) - 1 - index)))
            index -= 1

    elif operation == 'get_str':
        decr = input_var
        index = 0
        temp_value = []

        while decr > 0:
            temp_value.append(str(int(decr / 256 ** (3 - index))))
            decr %= (256 ** (3 - index))
            index += 1

        temp_value = '.'.join(temp_value)

    return temp_value


# Body
ip_start, ip_end = ip_addresses.split('-')

num_ip_s = ip_str_int(ip_start, 'get_int')
num_ip_e = ip_str_int(ip_end, 'get_int')

if num_ip_s <= num_ip_e:
    num_ip_t = num_ip_s

    print('Printing IP in range {}'.format(ip_addresses))

    while num_ip_t <= num_ip_e:
        ip_addr_str = ip_str_int(num_ip_t, 'get_str')

        print('IP is {}'.format(ip_addr_str))

        num_ip_t += 1

else:
    print('The starting IP in the range is higher than the final one.')

