hello = {"Pen", "Bag", "Book", "Eraser"}
world = {1, 2, 3, 4, "School", "Biro", "Pen", "Book"}

#newset = hello.union(world)
#hello.update(world)
#hello.intersection_update(world)
#newset = hello.intersection(world)
#hello.symmetric_difference_update(world)
newset = hello.symmetric_difference(world)
print(newset)
