student = {
    "name":"Ali",
    "age":21
}
print(student.get("name"))
print(student.get("cgpa", "Not Found"))
st2 = student.copy()

print(st2)

student.update(st2)
print(student)
keys = ["one", "two" ]
dct = dict.fromkeys(keys)
print(dct)

dct.setdefault("city" ,"islamabad")
print(dct)

