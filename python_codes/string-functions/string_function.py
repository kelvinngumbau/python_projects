#neccessary string functions
text = "I like you and you like me"
print(text.lower())#converts all letters into lower case
print(text.upper())#converts all the letters into upper case
print(text.capitalize())#converts first letter into upper case
print(text.title())#converts all the letters into titlecase

#count function
print(text.count("you"))# returns 2

#find function
print(text.find("you"))

#join function
text2 = ['mike','john','Anna']
text3 = "-"

#use join
print(text3.join(text2))

#replace function
text4 = "I like John and John is my friend"
print(text4.replace("John","Anna"))

#split function and put them into a list
names ="John,Max,Bob,Anna"
name_list = names.split(",")
print(name_list)#it print the result inform of a list