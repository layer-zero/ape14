#!/usr/bin/env python2


from jsonrpclib import Server

switch_ip = '10.0.0.6'
username = 'Script'
password = 'Arista'
eapi_url = 'https://{}:{}@{}/command-api'.format(username, password, switch_ip)

switch = Server(eapi_url)

response = switch.runCmds(1, ['show version'])

print 'The version is ' + response[0]['version']
