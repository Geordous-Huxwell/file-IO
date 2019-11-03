#r		Read Only. pointer at start of file (default)
#rb		same as r but in binary
#r+		reading and writing (pointer at begin)
#rb+	same as r+ but in binary

#w 		Writing only. overwrites file if exists. creates new file otherwise.
#wb		same as w but in binary
#w+		same as w plus reading
#wb+	same as w+ but in binary

#a 		open a file for appending if file does not exist create it
#ab		same as a but in binary
#a+		same as a plus reading
#ab+	same as a+ but in binary
import os
print(os.getcwd())
try:
	os.mkdir("Test folder")
except FileExistsError:
	print("That folder already exists")

myFile = open("README.txt","w")
print(myFile.name)
print(myFile.closed)
print(myFile.mode)
myFile.write("Hello everyone. python is so much fun.\r\nthis text is on a new line.\r\n\tthis text is on a new line and tabbed over.\r\n\"this text is in quotes somehow\"")
#myFile.write("Jordan Doerksen is hungry")
myFile.close()
print(myFile.closed)

myFile = open("README.txt","r")
print("file is",os.stat("README.txt").st_size,"bytes large")
print(myFile.read(os.stat("README.txt").st_size))

myFile.close()