#!/usr/bin/python3

# create egoad with password of Password01

import pexpect

# connect and log in to db1
child = pexpect.spawn('ssh 192.168.0.121')
child.expect('.*password:')
child.sendline('Password01')
print('Logged into db1  successfully')

# create egoad user and password
child.expect('\[.*~\]\$')
child.sendline('sudo adduser egoad')
child.expect('\[sudo\] password for justincase:')
child.sendline('Password01')
print('egoad created')
child.expect('\[.*~\]\$')
child.sendline('sudo passwd egoad')
child.expect('New password:')
child.sendline('Password01')
child.expect('Retype new password:')
child.sendline('Password01')
print('password changed')

# logout
child.expect('\[.*~\]\$')
child.send('exit')
print('logged out of db1')

# connect and log in to db2
child = pexpect.spawn('ssh db2.local')
child.expect('.*password:')
child.sendline('Password01')
print('Logged into db2 successfully')

# create egoad user and password
child.expect('\[.*~\]\$')
child.sendline('sudo adduser egoad')
child.expect('\[sudo\] password for justincase:')
child.sendline('Password01')
print('egoad created')
child.expect('\[.*~\]\$')
child.sendline('sudo passwd egoad')
child.expect('New password:')
child.sendline('Password01')
child.expect('Retype new password:')
child.sendline('Password01')
print('password changed')

# logout
child.expect('\[.*~\]\$')
child.send('exit')
print('Logged out of db2')

# connect and log in to web1
child = pexpect.spawn('ssh web1.local')
child.expect('.*password:')
child.sendline('Password01')
print('Logged into web1 successfully')

# create egoad user and password
child.expect('\[.*~\]\$')
child.sendline('sudo adduser egoad')
child.expect('\[sudo\] password for justincase:')
child.sendline('Password01')
print('egoad created')
child.expect('\[.*~\]\$')
child.sendline('sudo passwd egoad')
child.expect('New password:')
child.sendline('Password01')
child.expect('Retype new password:')
child.sendline('Password01')
print('password changed')

# logout
child.expect('\[.*~\]\$')
child.send('exit')
print('Logged out of web1')

# connect and log in to web2    
child = pexpect.spawn('ssh web2.local')
child.expect('.*password:')
child.sendline('Password01')  
print('Logged into web2 successfully')

# create egoad user and password   
child.expect('\[.*~\]\$')
child.sendline('sudo adduser egoad')
child.expect('\[sudo\] password for justincase:')
child.sendline('Password01')
print('egoad created')
child.expect('\[.*~\]\$')
child.sendline('sudo passwd egoad')
child.expect('New password:')
child.sendline('Password01')
child.expect('Retype new password:')
child.sendline('Password01')
print('password changed')

# logout
child.expect('\[.*~\]\$')
child.send('exit')
print('Logged out of web2')

