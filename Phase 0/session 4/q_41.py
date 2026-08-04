num = 123456
sum_ = 0
count = 0 
while num != 0:
    dig = num % 10
    sum_ += dig
    count += 1
    num = num//10

print(f"sum: {sum_}, count: {count}")