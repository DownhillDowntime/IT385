#!/usr/bin/python3

# 3 example of writing a file in Python

# open the file
myFile = open("testfile.txt", "w")

# write to the file
myFile.write("Hello Worlding\n")
myFile.write("wheel snipe\n")
myFile.write("Celly bois\n")

# close the file
myFile.close()
