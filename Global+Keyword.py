x = "Peter"

def hello():
    global x
    x = "Paul"

hello()
print(x)
