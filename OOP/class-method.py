class Employee:        #template
    ClassIncrement = 1.2 # class variable
    def __init__(self,fname,lname,salary): #constructor
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.InstanceIncrement = 1.5 # instance variable

    def promotion(self):
        self.salary = int( self.salary * self.InstanceIncrement)
    def masspromotion(self):
        self.salary = int(self.salary * Employee.ClassIncrement)

    @classmethod  #decorator
    def change_ClassIncrement(cls,amount):
        cls.ClassIncrement = amount


# creating objects

jay = Employee('jay','chavan',66000)
jayesh = Employee('jayesh','chavan',75000)

print(jay.fname)
print(jayesh.salary)
print(' ')
print(jay.salary)
jay.promotion()
print(jay.salary)
print(' ')
print(jayesh.salary)
jayesh.masspromotion()
print(jayesh.salary)

print(jay.salary)
Employee.change_ClassIncrement(3) # function in Employee class 
jay.masspromotion()
print(jay.salary)