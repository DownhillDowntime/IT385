#!/usr/bin/python3

# script using pxssh to get uptime

from pexpect import pxssh

# login

s = pxssh.pxssh()
s.login('192.168.0.111','justincase','Password01')
print('SSH login successful')

# run command
s.sendline('uptime')
s.promt()
s=print(s.before)

# logout
s.logout()
