#!/usr/bin/python3
# password generator

import random
import string

def password(size=10, chars=string.ascii_letters + string.punctuation + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
 
print("Your First Password Is", password())
print("Your Second Password Is", password())
