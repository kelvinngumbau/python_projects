#string formatting in python
#%c, character
#%s string
#%d or %i, integer
#%f, float
#%e, exponential notation

name, age = 'kelvin mwako', 45
print("my name is %s "%name)
print("I am %d years old"%age)

#use format, makes it more general without specifying data types
name2, age2 = 'James', 90
#here we use curly brackets as placeholder
print("my name is {} and i am {} years old".format(name2,age2))
 