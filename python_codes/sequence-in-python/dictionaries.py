#dictionary 
#written in curly brackets
dict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 2014
}

print(dict)
#to print only one value we use square bracket[]
print(dict["brand"])
#print length len()
print(len(dict))

#type, print data types
print(type(dict))

#another method to access a key
x = dict["year"]
print(x)

#also we can use get() method to acheive the same
x = dict.get("year")
print(x)

#get key
n = dict.keys()
print(n)

#get values
m = dict.values()
print(m)

#modify a value from a dictionary
dict["year"] = 2018
print(dict)
#get values
print(dict.values())

#check if the key exist
if "year" in dict:
    print(dict["year"])
else:
    print("year does not exist")

#dict.copy(), returns a copy of the dictionary
dict1 = dict.copy()
print(dict1)
#dict.clear(), removes all elements from a dictionary

