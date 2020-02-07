#!/usr/bin/python3

# example PEXPECT Script from FTP

import pexpect

# open connection and login
child = pexpect.spawn('ftp ftp.redhat.com')
child.expect('Name.*:')
child.sendline('ftp')
child.expect('Password:')
child.sendline('ftp')

# cd and download file
child.expect('ftp>')
child.sendline('cd pub/redhat/linux/enterprise/7Server/en/Ansible')
child.expect('ftp>')
child.sendline('get ansible-2.5.7-1.el7ae.src.rpm')

# quit
child.expect('ftp.')
child.sendline('quit')
