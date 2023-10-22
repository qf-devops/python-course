hello = ("Pen", "Pencil", "Book", "Eraser", "Bag")
x = list(hello)
"""
x.append("Biro")
hello = tuple(x)
"""
"""
x[3] = "Biro"
hello = tuple(x)
"""
"""
x.remove("Book")
hello = tuple(x)
"""

print(hello)