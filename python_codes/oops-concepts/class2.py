#class basic information

class Person:
    def __init__ (self , name , age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def basic_info(self):
        print("Name: {}\n Age: {}\n Sex: {}\n".format(self.name,self.age,self.sex))

person1 = Person("Kelvin Mwako",45,"Male")
person1.basic_info()
