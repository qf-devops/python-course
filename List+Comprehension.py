hello = ["Pen", "Book", "Bag", "Pencil", "Eraser"]

"""
for x in hello:
    if "a" in x:
        world.append(x)

print(world)"""
#world = [x for x in hello if x != "Pen"]
#world = [x for x in hello]
#world = [x for x in range(20)]
#world = [x for x in range(20) if x >= 10]
#world = [x.upper() for x in hello]
#world = ["School" for x in hello]
world = [x if x != "Eraser" else "School" for x in hello]

print(world)