file = open('./student.txt', "w")
file.write("hello world")

file.close()

file = open('./student.txt', 'a')
file.write("this is the appended thing")
file.close()

# file = open("./newfile.txt", "x")
# file.close()

with open("student.txt", "r") as f:
    print(f.read())

f.close()
# checking if file exits os.path.exists("student.txt")

# deleting a file os.remove("student.txt")

# renaiming os.rename("old.txt", "new.txt")
