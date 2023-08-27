#writing into a file using python
#performing access mode

file = open("file-operation/myfile2.txt","w")
print(file.write("Hello everyone, we appreciate your efforts guys"))
#we flush so that the text gets written
file.flush()
file.close()