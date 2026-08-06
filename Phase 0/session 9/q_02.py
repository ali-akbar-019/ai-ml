info = {
    "name": "ali",
    "age": 22,
    "city": "islamabad"
}
info["age"] = 22.2
print(info)
info.pop("city")
print(info)
info.popitem()
print(info)

print(info)
info.clear()
print(info)