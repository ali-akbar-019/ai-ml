name = input("Enter a name")
dct = {}
dct["name"] = name
print(dct)

dct2={}
for i in range(3):
    name = input("Enter a name: ")
    age = int(input("Enter age: "))
    dct2[name] = age

print(dct2)