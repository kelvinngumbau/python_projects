#overwriting in python

class Animal:
    def __init__(self, name):
        self.name = name
    
    #method make sound
    def make_sound(self):
        print("make sound")
        
class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__ (name)
        
    #overwriting make sound method
    def make_sound(self):
        print("dog bark")
        print("{}".format(self.name))

animal = Dog("dog")
animal.make_sound()