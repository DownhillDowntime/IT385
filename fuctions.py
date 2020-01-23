#!/usr/bin/python3

# basic function
def func1():
	print("Getting Functy")

#function that takes an argument
def addNums(val1, val2):
	print(val1 + val2)

#fuction with a default value
def power(num, power=2):
	result = 1
	for i in range(power):
		result = result * num
	print(result)

#function that returns a value
def cube(x):
	return x * x * x

#function that adds variable number of  numbers
def multi_add(*args):
	result = 0
	for x in args:
		result = result + x
	return result

#call functions

print(multi_add(6, 7))
print(multi_add(15, 38, 22, 67))

#cube(3)
#print(cube(5))
#myCube = cube(7)
#print(myCube)

#func1()
#print(func1())
#print(func1)

#addNums(7, 11)

#power(5)
#power(5, 2)
#power(5, 3)
