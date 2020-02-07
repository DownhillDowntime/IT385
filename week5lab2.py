#!/usr/bin/python3

# script to install, run, and set to autostart apache on web servers

from pexpect import pxssh

#login to web1

s = pxssh.pxssh()
s.login('192.168.0.111','justincase','Password01')
print('login to web1 successful')

# run apache commands

s.sendline('sudo yum install httpd')
s.prompt()
s.sendline('Password01')
s.prompt()
s.sendline('sudo service httpd start')
s.prompt()
s.sendline('sudo chkconfig --level 345 httpd on')
print(s.before)
print('apache install and setup complete')

# logout of web1
s.logout()
print('logged out of web1')

# login to web2

s = pxssh.pxssh()
s.login('192.168.0.112','justincase','Password01')
print('login to web2 successful')

# run apache commands

s.sendline('sudo yum install httpd')
s.prompt()
s.sendline('Password01')
s.prompt()
s.sendline('sudo service httpd start')
s.prompt()
s.sendline('sudo chkconfig --level 345 httpd on')
print(s.before)
print('apache install and setup complete')

# logout of web2
s.logout()
print('logged out of web2')

