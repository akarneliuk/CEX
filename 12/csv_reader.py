#!/usr/local/bin/python3.8

# Modules
import sys
from re import *
from csv import DictReader

# Body
if len(sys.argv) < 2:
    sys.exit('You haven\'t provided the path to the file.')

elif len(sys.argv) > 2:
    sys.exit('You have provied too many arguments.')

else:
    if match('.*\.csv$', sys.argv[1]):
        ld = []

        with open(sys.argv[1], 'r') as f:
            reader = DictReader(f)

            for row in reader:
                ld.append(row)

        print(ld)

    else:
        sys.exit('The provided file doesn\'t have \'.csv\' extension.')
        