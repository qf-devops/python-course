class Company:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def Employee(self):
        print("Your name is " + self.firstname + " " + self.lastname + " Your age is " + str(self.employmentage))

class Worker(Company):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.employmentage = age

Comp = Worker("Peter", "Paul", 24)
Comp.Employee()