#!/usr/bin/env python2
""" This script uses the JSON library to pretty print a dictionary."""

# Import the JSON library.
import json

# Define the dictionary.
foo = {
        'Marbles': ['Blue', 'Red', 'Yellow'],
        'Name': 'Bob ',
        'Stats':    {
                    'Age': 12,
                    'Eyes': 'Blue',
                    'Sex': 'Male'
                    }
        }

# Convert the dictionary to a JSON string using an indent of 4 and print
# the JSON string.
print json.dumps(foo, indent=4)
