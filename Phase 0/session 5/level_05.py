text = "this is hte ext that we are going to use "

for i in text:
    print(i)

vowels = 'aeiou'
countConsonents = 0
for i in text:
    if i not in vowels:
        countConsonents+=1

print("Consonents: ", countConsonents)

uppercaseLetters = 0
lowercaseLetters = 0
for i in text:
    if i >= 'A' and i <= 'Z':
        uppercaseLetters+=1
    else:
        lowercaseLetters+=1

print("Upper case letters: ",uppercaseLetters)
print("Lower case letters: ",lowercaseLetters)

digits = 0
for i in text:
    if i.isdigit():
        digits+=1

print("digits: ", digits)

spaces = 0
for i in text:
    if i == " ":
        spaces+=1

print("spaces: ", spaces)
