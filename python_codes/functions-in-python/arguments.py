#function with arguments

def my_function(fname):
    print( fname + " Mwako")
    
#call the function three times
my_function("Kelvin")
my_function("Musyoka")
my_function("Kituku")

#by default a function must be called by the correct number of arguments not less or more than the arguments
def my_function(fname,lname):
    print("hello " + fname + lname)
my_function("kelvin"," mwako")

#we use asteric * if we dont know the number of arguments to be passed

def my_function(*kids):
    print("my child name is " + kids[2])
my_function("Emily","Rashford","Greenwood","Lucky Dube")

#the order of arguments does not matter

def my_function(child3,child2,child1):
    print("my second child is " + child2)
my_function(child1='James',child2='Mount',child3='Pulisic')

#if you dont know how many keywords arguments that will be passed into your function use two asterisk **
