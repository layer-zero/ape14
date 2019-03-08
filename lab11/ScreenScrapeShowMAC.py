#!/usr/bin/env python2

import pexpect

hostname = '10.0.0.6'
username = 'Script'
password = 'Arista'

ssh_options = ['-l ' + username,
               '-o UserKnownHostsFile=/dev/null',
               '-o StrictHostKeyChecking=no']
ssh_command = 'ssh ' + ' '.join(ssh_options) + ' ' + hostname

c = pexpect.spawn(ssh_command)

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
