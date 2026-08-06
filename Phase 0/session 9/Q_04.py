student = {
    "name":"Ali",
    "age":21
}
for key in student.keys():
    print(key)


for val in student.values():
    print(val)

for k,v in student.items():
    print(k,":",v)

for v in student.values():
    if(type(v) == int):
        print(v)

for v in student.values():
    if(type(v) == str):
        print(v)

for k,v in student.items():
    if type(v)== int and v > 20:
        print(k)