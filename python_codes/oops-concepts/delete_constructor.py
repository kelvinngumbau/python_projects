#delete constructor in python

class Car:
    car_amount = 0
    def __init__(self , manufacturer, model, hp):
        self.manufacturer = manufacturer
        self.model = model
        self.hp = hp
        Car.car_amount +=1
    #constructor
    def basic_info(self):
        print("{}\n{}\n{}\n".format(self.manufacturer,self.model,self.hp))
        
    def print_car_amount(self):
        print("amount of cars {}".format(Car.car_amount))
    
    
    #creating destructor, we use del function
    
    def __del__(self):
        Car.car_amount -=1
                
car1 = Car('Tesla','Model x',525)
car2 = Car('BMW','x3',200)
car3 = Car('VW','Golf',100)
car4 = Car('Porsche','911',520)
#deleting car4 using delete constructor
del car4
car1.basic_info()
car1.print_car_amount()