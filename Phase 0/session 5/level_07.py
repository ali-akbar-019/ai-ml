vowels= "aeiou"
text = " this ist he text and i am gonna do someting in this challange  file"
# count the number of hte vowesl occurances
for i in vowels:
    print(i,":",text.count(i))


# remove all the vowels from the string
print(text)
for i in vowels:
    text.replace(i, "")
print(text)

# reverse every word in a sentence while keeping the word order the same

words = text.split(' ')
words = [word[::-1] for word in words]
text = " ".join(words)
print("after reversing each word\n",text)

# check if anagrams
text = "something"
revText = text[::-1]
isAnagram = sorted(text) == sorted(revText)
print("is anagram: ", isAnagram)