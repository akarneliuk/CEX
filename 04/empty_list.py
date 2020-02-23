#!/usr/local/bin/python3.8

network_functions = []

print('Your list is: {}'.format(network_functions))

network_functions.append('Router1')
print('Your list is: {}'.format(network_functions))

network_functions.append('Router2')
print('Your list is: {}'.format(network_functions))

network_functions.extend(['Router3', 'Router4'])
print('Your list is: {}'.format(network_functions))

temp_value = network_functions.pop(1)
print('Your list is: {} and removed element is {}'.format(network_functions, temp_value))

temp2 = network_functions.remove('Router3')
print('Your list is: {} and removed element is {}'.format(network_functions, temp2))

