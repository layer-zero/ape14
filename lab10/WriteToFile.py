#!/usr/bin/env python2


with open('Lumberjack.txt', 'a') as lumberfile:
    # Using "()" allows you to split string literals across lines with
    # arbitrary indentation for better readability and PEP-8 compliance.
    # Note that "extralines" is still a simple string.
    extralines = ('He cuts down trees, he eats his lunch,\n'
                  'He goes to the lava-try.\n')
    lumberfile.write(extralines)
