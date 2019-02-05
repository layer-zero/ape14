#!/usr/bin/python

# Import the pretty print function
from pprint import pprint

# Define the dictionary
foo = {
        'Marbles': ['Blue', 'Red', 'Yellow'],
        'Name': 'Bob ',
        'Stats':    {
                    'Age': 12,
                    'Eyes': 'Blue',
                    'Sex': 'Male'
                    }
        }

# Pretty print the dictionary
pprint(foo)
