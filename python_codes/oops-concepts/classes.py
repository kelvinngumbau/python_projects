#classes and objects in python
#class name car
#every function of a class has to self parameter and is mandatory
class Car:
    def __init__ (self, manufacturer,model,hp):
        self.manufacturer = manufacturer
        self.model = model
        self.hp = hp
        
    #creating another function
    def print_info(self):
        print("Manufacturer: {},'\n' model {},'\n' HP; {}".format(self.manufacturer, self.model, self.hp))
    #we have created the class now we are creating the object
    
mycar = Car("Hp manufacturer","Vostro 1540","Hp")
mycar.print_info()
        