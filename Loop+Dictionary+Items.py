student = {"school" : "Academy",
           "name" : "Peter",
           "class" : 4,
           "age" : 18,
           "pupil": ["Paul", "Mike", "Hello", "World"]}
"""
for x in student:
    print(x)
"""
"""
for x in student.keys():
    print(x)
"""
"""
for x in student:
    print(student[x])
"""
"""
for x in student.values():
    print(x)"""
"""
for x,y in student.items():
    print(x,y)"""
#mystud = student.copy()
hellostudent = dict(student)
print(hellostudent)