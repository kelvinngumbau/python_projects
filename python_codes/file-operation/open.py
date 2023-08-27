#opening a file

file = open("myfile.txt","r")
#reading from the file, we only use read() method
print(file.read())
#closing our file
file.close()