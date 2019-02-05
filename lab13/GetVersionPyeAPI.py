#!/usr/bin/env python2


import pyeapi

pyeapi.load_config('Targets.conf')
student_switch = pyeapi.connect_to('Student-06')

response = student_switch.enable(['show version'])

print response[0]['result']['version']
