#!/usr/local/bin/python3.8

# Variables

ip_addresses = '10.0.0.3-10.0.1.15'

ip_start, ip_end = ip_addresses.split('-')

ip_start = ip_start.split('.')
index = len(ip_start) - 1
num_ip_s = 0

while index >= 0:
    num_ip_s += (int(ip_start[index]) * (256 ** (len(ip_start) - 1 - index)))
    index -= 1

ip_end = ip_end.split('.')
index = len(ip_end) - 1
num_ip_e = 0

while index >= 0:
    num_ip_e += (int(ip_end[index]) * (256 ** (len(ip_end) - 1 - index)))
    index -= 1

if num_ip_s <= num_ip_e:
    num_ip_t = num_ip_s

    print('Printing IP in range {}'.format(ip_addresses))

    while num_ip_t <= num_ip_e:
        decr = num_ip_t
        ind = 0
        temp_ip_l = []

        while decr > 0:
            temp_ip_l.append(str(int(decr / 256 ** (3 - ind))))
            decr %= (256 ** (3 - ind))
            ind += 1

        print('IP is {}'.format('.'.join(temp_ip_l)))

        num_ip_t += 1

else:
    print('The starting IP in the range is higher than the final one.')

