text = "this is the level 3 string methods"

print(text.upper())
print(text.lower())
print(text.title())
print(text.strip())
print(text.replace("t", "a"))
print(text.replace(" ", "_"))
print(text.count('e'))
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for i in text:
    count += text.count(i)

print("count of vowels: ", count)
print(text.find("Python"))