text = "NooN"
if text == text[::-1]:
    print("Palindrome")

text = "banana"
from collections import Counter
freq = Counter(text)
print(freq)


text = " thi is me and i am a good man"
print(text.replace(" ", ""))

maxWord = ""
for i in text.split(' '):
    if len(i) > len(maxWord):
        maxWord = i

print("max word: ", maxWord)

name = input("Enter your name")
initials = name.split(' ')[0][0].upper() +"."+ name.split(' ')[1][0].upper()
print("Name: ", name, "\nInitials: ",initials)

