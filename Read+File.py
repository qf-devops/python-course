"""
f = open("C:/Users/USER/Desktop/PyFile/Demo2.txt", "w")
f.write("Welcome to python programming. This is a testing file writer")
f.close()"""

f = open("C:/Users/USER/Desktop/PyFile/Demo1.txt", "r")
#print(f.readline())
for x in f:
    print(x)

f.close()
