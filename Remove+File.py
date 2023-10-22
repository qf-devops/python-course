import os

#Delete Files
if os.path.exists("C:/Users/USER/Desktop/PyFile/Demo.txt"):
    os.remove("C:/Users/USER/Desktop/PyFile/Demo.txt")
else:
    print("File path does not exist")

#Delete Folder
os.rmdir("C:/Users/USER/Desktop/PyFile/")