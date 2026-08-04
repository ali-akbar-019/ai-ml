name = "Ali"

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[-1])
# print(name[-2])
# print(name[-3])
# in python negative indexing also works

# len
print(len(name))

# slicing
# start: end + 1 : steps
text = "my favorite movie is dune part 2"
print(text[0:])
print(text[5:])
print(text[0:10])
print(text[0:10:2])
print(text[: :-1])

# concatination
first = "ali"
last = "akbar"
print(first+ " " + last)
print("*"*10)

# member ship operators
text = "python"
print("o" in text)

# common string methods
# upper
name = "ali akbar"
print(name.upper())
# lower
print(name.lower())
# title
print(name.title())
# capitalize
print("name is akbar".capitalize()) 
# strip
name = "                   ali                         "
print(name)
print(name.strip())
# replace
print(name.replace("ali", "zarak"))
# count
print(name.count('a'))
# find - returns the first index of a substring
# not found pe -1 throw karta ha ye
print(text.find('a'))

# starts with and ends with
text = "ali akbar is learning python"
print(text.startswith("a"))
print(text.endswith("za"))
# escape characters
print("I \" this is escape")

# loop
for i in text:
    print(i)