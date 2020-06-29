#!/usr/local/bin/python3.8

# Variables
path_to_file = './some_data.csv'

# Body
## Reading and parsing
with open(path_to_file, 'r') as f:
    file_content = f.read()

data_lines = file_content.split('\n')
header_keys = data_lines.pop(0).split(',')

result_data = []

for data_line in data_lines:
    temp_dict = {}

    for entry_index, entry_value in enumerate(data_line.split(',')):
        temp_dict.update({header_keys[entry_index]: entry_value})

    result_data.append(temp_dict)

## Create spreadsheet and write
t0 = []

for line_index, line_entry in enumerate(result_data):
    t1 = []
    t2 = []

    for item_key, item_value in line_entry.items():
        if line_index == 0:
            t1.append(item_key)

        t2.append(item_value)

    if t1:
        t0.append(','.join(t1))

    t0.append(','.join(t2))

with open('./new_file.csv', 'w') as f:
    f.write('\n'.join(t0))