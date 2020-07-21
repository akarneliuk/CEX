#!/usr/local/bin/python3.8

# Modules
import sys
from csv import DictReader
from re import *

# Body
if len(sys.argv) < 2:
    sys.exit('You havn\'t provided any arguments.')

elif len(sys.argv) > 2:
    sys.exit('You have provided too many arguments.')

else:
    if match('.*\.csv$', sys.argv[1]):
        ld = []
        with open(sys.argv[1], 'r') as f:
            csv_dict = DictReader(f)

            for entry in csv_dict:
                ld.append(entry)

        print(ld)

    else:
        sys.exit('The provided file is not .csv.')