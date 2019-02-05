#!/usr/bin/env python2


with open('Lumberjack.txt', 'r') as lumberfile:
    lumberlines = lumberfile.readlines()
for line in lumberlines:
    print line,
