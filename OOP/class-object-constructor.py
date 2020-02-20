class Employee:        #template
    def __init__(self,fname,lname,salary): #constructor
        self.fname = fname
        self.lname = lname
        self.salary = salary

# creating objects

jay = Employee('jay','chavan',66000)
jayesh = Employee('jayesh','chavan',75000)

print(jay.fname)
print(jayesh.salary)