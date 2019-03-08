#!/usr/bin/env python2

import jsonrpclib

switch_ip = '10.0.0.6'
username = 'Script'
password = 'Arista'
commands = ['enable', 'configure', 'boot system flash:NoSuchFile']

eapi_url = 'https://{}:{}@{}/command-api'.format(username, password, switch_ip)

switch = jsonrpclib.Server(eapi_url)

try:
    response = switch.runCmds(1, commands)
except jsonrpclib.jsonrpc.ProtocolError as error:
    print 'Error code {}: {}'.format(error[0][0], error[0][1])
else:
    print 'The version is ' + response[0]['version']
