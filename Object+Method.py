class Boss:
    def __init__(self, fname, age):
        self.fname = fname
        self.age = age

    def Hello(self):
        print("Welcome " + self.fname + ". " + "Your age is " + str(self.age))

BH = Boss("Peter", 40)
BH.Hello()