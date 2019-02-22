#!/usr/bin/env python2

import pexpect

hostname = '10.0.0.6'
username = 'Script'
password = 'Arista'

c = pexpect.spawn('ssh ' + '-l ' + username + ' ' + hostname)

c.expect('Password')
c.sendline(password)
c.expect('>')
c.sendline('enable')
c.expect('#')
c.sendline('show version')
c.expect('#')

output = c.before.replace('\r', '')

for line in output.splitlines():
    if 'MAC address' in line:
        print line
