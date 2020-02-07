#!/usr/bin/python3

# script that reads a file

# easy reading of a file
myFile = open("testfile.txt", "r")
print(myFile.read())
myFile.close()

# reading file line by line
myFile = open("testfile.txt", "r")
for line in myFile:
	print(line)
myFile.close()

# print lines that start with a specific character/search through a file

myFile = open("testfile.txt", "r")
for line in myFile:
	if line.startswith("w"):
		print(line)
myFile.close()

# read a file using a WITH statement

with open("testfile.txt", "r") as myFile:
	print(myFile.read())




















