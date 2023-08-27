#inhritance

#class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def details(self):
        print("name {}\n Age {}".format(self.name,self.age))
        
    #function get_order()
    def get_order(self, years):
        
        self.age +=years
        
class Students(Person):
    def __init__(self, name, age,language):
        super(Students,self). __init__(name, age)
        self.language = language
        
    def print_language(self):
        print("your favorite programming language {}".format(self.language))

p1 = Students("kelvin", 45, "python")
print(p1.name)
print(p1.age)
print(p1.language)
p1.details()
p1.get_order(68)
print(p1.age)

