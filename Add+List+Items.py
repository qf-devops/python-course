hello = ["Pen", "Book", "Bag", "Pencil"]
World = ["Python", "Java", "C#", "C++", "PHP"]
TupMore = ("Exam", "Quiz", "Paper")
#hello.insert(0, "Eraser")
#hello.append("Biro")

World.extend(TupMore)

print(World)