#!/usr/bin/python3

# sample script that gets hostnames

import pexpect

# connect and log in
child = pexpect.spawn('ssh 192.168.0.111')
child.expect('.*password:')
child.sendline('Password01')
print('Logged in successfully')

# run hostname command
child.expect('\[.*~\]\$')
child.sendline('hostname')
# print(child.before) incorrect placement of this
print('Ran hostname command')

# logout
child.expect('\[.*~\]\$')
print(child.before)
child.sendline('exit')
print('Logged out')

