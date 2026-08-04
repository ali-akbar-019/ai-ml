odd_count = 0
even_count = 0
n = int(input("N: "))
for i in range(1, n+1):
    if i % 2 == 1:
        odd_count +=1
    else:
        even_count +=1

print("even count: ",even_count)
print("odd count: ", odd_count)
