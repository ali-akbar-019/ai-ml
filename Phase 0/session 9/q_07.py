text = "banana"
freq= {}
for t in text:
    freq[t] = freq.get(t, 0) + 1

print(freq)

sentence = "I love python and I love AI"
sentence_list = sentence.split(" ")

for word in sentence_list:
    freq[word] = freq.get(word, 0) + 1

print(freq)