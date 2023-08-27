#reading from a file using with
with open("myfile.txt","r") as file:
    print(file.read())
file.close()