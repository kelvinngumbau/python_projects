#try except in python
#used to handle exception or errors in python

try:
    result = 10/0
    text = 'hello'
    #perform typecasting of text into int
    name = int(text)
except ZeroDivisionError:
    print("a number divided by zero is zero")

except ValueError:
    
    print("a string cannot be typecasted into an integer value")
else:
    
    print("performing basic try except examples in python")


