#!/usr/local/bin/python3.8

# Variables
path_to_file = './some_data.csv'

# Body
## Reading CSV file and parsing it into Python data structures
with open(path_to_file, 'r') as f:
    file_content = f.read()

data_lines = file_content.split('\n')
headers = data_lines.pop(0)
headers_keys = headers.split(',')

result_data = []

for line_entry in data_lines:
    temp_dict = {}

    for value_index, value_entry in enumerate(line_entry.split(',')):

        temp_dict.update({headers_keys[value_index]: value_entry})
    
    result_data.append(temp_dict)

print(result_data)

## Converting Python data into CSV format and writing into a file
t0 = []

for line_index, data_entry in enumerate(result_data):
    t1 = []
    t2 = []
    for key, value in data_entry.items():
        if line_index == 0:
            t1.append(key)

        t2.append(value)

    if t1:
        t0.append(t1)

    t0.append(t2)

t4 = [','.join(t0_entry) for t0_entry in t0]


with open('new_file.csv', 'w') as f:
    f.write('\n'.join(t4))