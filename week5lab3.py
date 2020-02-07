#!/usr/bin/python3

#install and setup mysql on db servers

from pexpect import pxssh

# login to db1

s = pxssh.pxssh()
s.login('192.168.0.121','justincase','Password01')
print('login to db1 successful')

# install and setup mysql
s.sendline('sudo rpm -Uvh https://repo.mysql.com/mysql80-community-release-el7-3.noarch.rpm')
s.prompt()
s.sendline('Password01')
s.prompt()
s.sendline('sudo yum --enablerepo=mysql57-community install mysql-community-server')
s.prompt()
s.sendline('y')
s.prompt()
s.sendline('y')
s.prompt()
s.sendline('sudo service mysqld start')
s.prompt()
s.sendline('Password01')
s.prompt()
s.sendline('sudo chkconfig --level 345 mysqld on')
s.prompt()
s.sendline('Password01')
s.prompt()
print('MySQL install and setup complete')

# logout of db1
s.logout()
print('logout of db1 successful')


# login to db2

s = pxssh.pxssh()
s.login('192.168.0.122','justincase','Password01')
print('login to db2 successful')

# install and setup mysql
s.sendline('sudo rpm -Uvh https://repo.mysql.com/mysql80-community-release-el7-3.noarch.rpm')
s.prompt()
s.sendline('Password01')
s.prompt()
s.sendline('sudo yum --enablerepo=mysql57-community install mysql-community-server')
s.prompt()
s.sendline('y')
s.prompt()
s.sendline('y')
s.prompt()
s.sendline('sudo service mysqld start')
s.prompt()
s.sendline('Password01')
s.prompt()
s.sendline('sudo chkconfig --level 345 mysqld on')
s.prompt()
s.sendline('Password01')
s.prompt()
print('MySQL install and setup complete')

# logout of db2
s.logout()
print('logout of db2 successful')

