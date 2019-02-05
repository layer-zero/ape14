#!/usr/bin/env python2

from time import sleep
from jsonrpclib import Server

switch_ip = '10.0.0.6'
username = 'Script'
password = 'Arista'
commands = ['show version']

eapi_url = 'https://{}:{}@{}/command-api'.format(username, password, switch_ip)

switch = Server(eapi_url)

try:
    sleep(5)
    response = switch.runCmds(1, commands)
except KeyboardInterrupt:
    print '\nCaught ^C: exiting'
else:
    print 'The version is ' + response[0]['version']
