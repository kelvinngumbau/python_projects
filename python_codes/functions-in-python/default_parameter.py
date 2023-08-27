#default parameter
def my_function(country = "Kenya"):
     print("my country is " + country)
     
my_function("sudan")
my_function("Uganda")
my_function()#default parameter will be called that is Kenya
my_function("Tanzania")

#passing list as an argument
def my_function(food):
    for x in food:
        print(x)
fruits = ['mangoes','apples','oranges','lemon','banana']

my_function(fruits)