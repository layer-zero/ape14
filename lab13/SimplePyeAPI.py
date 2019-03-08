#!/usr/bin/env python2


import pyeapi

connection = pyeapi.connect(host='Student-06')
response = connection.execute(['enable', 'show version'])
print response['result'][1]['version']
