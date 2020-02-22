#!/usr/local/bin/python3.8

network_functions = ['PE1-BLN-DE', 'PE2-BLN-DE', 'de-bln-eq1-leaf101', 'de-bln-eq1-leaf102', 'sw1-s1-hq-bln', 'sw2-s1-hq-bln']

print('All the network functions in the network: {}'.format(network_functions))

print('The following devices are the service provider routers: {}, {}'.format(network_functions[0], network_functions[1]))
print('The following devices are the data centre switches: {}, {}'.format(network_functions[2], network_functions[3]))
print('The following devices are the enterprise campus switches: {}, {}'.format(network_functions[4], network_functions[5]))

value = network_functions.pop(0)
print('We have removed: {} and left: {}'.format(value, network_functions))

value1 = network_functions.remove('de-bln-eq1-leaf101')
print('We have removed: {} and left: {}'.format(value1, network_functions))

network_functions_new = []
print('Current network functions: {}'.format(network_functions_new))

network_functions_new.extend(['XR1'])
print('Current network functions: {}'.format(network_functions_new))

network_functions_new.append('SR1')
print('Current network functions: {}'.format(network_functions_new))


