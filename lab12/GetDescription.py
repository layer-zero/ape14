#!/usr/bin/env python2


from jsonrpclib import Server

switch_ip = '10.0.0.6'
username = 'Script'
password = 'Arista'
interface = 'Ethernet5'
commands = ['show interfaces ' + interface]

eapi_url = 'https://{}:{}@{}/command-api'.format(username, password, switch_ip)

switch = Server(eapi_url)

response = switch.runCmds(1, commands)

description = response[0]['interfaces'][interface]['description']
print 'The description on interface {} is {}'.format(interface, description)
