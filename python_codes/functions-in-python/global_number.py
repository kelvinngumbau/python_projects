#global number
#used to access a variable declared outside of the function
number = 10

def my_function():
    
    print(number)
my_function()

def my_function2():
    global number
    print(number)
my_function2()