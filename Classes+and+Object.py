"""
class hellas:
    num = 6

ella = hellas()
print(ella.num)"""

class hellonmade:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

world = hellonmade("Peter", "Paul")
#world.fname = "John"
print("your name is " + world.fname + " " + world.lname)