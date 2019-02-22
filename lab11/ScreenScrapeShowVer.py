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

raw_output = c.before.replace('\r', '')

output_list = raw_output.splitlines()

print '\n'.join(output_list[1:-1])
