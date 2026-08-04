for i in range(1, 11):
    print(i, end="\t")

print()

for i in range(10, 0, -1):
    print(i, end="\t")


print("all the even numbers from 1 to 50")
for i in range(1, 51):
    if i % 2 == 0:
        print(i)


print("All the odd numbers from 1 to 50")
for i in range(1, 51):
    if i % 2 == 1:
        print(i)


name = "ali"
for i in range(10):
    print(name)

print("Print numbers from 50 to 0 with a step of 5.")
for i in range(50, -1, -5):
    print(i)