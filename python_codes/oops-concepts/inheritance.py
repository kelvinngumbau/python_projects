class Person:
    count_people = 0
    def __init__(self, fname,lname):
        self.firstname = fname
        self.lastname = lname
        Person.count_people +=1
    def peoples_info(self):
        print("Full Name {} {}".format(self.firstname,self.lastname))
    
    def people_count(self):
        print("Total No of People {}".format(Person.count_people))
    
    def __del__(self):
        Person.count_people -=1
        

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation = year
        
    def Study(self):
        print("Graduation year: {}".format(self.graduation))
    
person1 = Person("kituku ", "Mwako ")
person1.peoples_info()
person1.people_count()
person2 = Student("kituku","Mwako",1999)
person2.Study()