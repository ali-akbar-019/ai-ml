# ask user for hte numbers and add to the list

nums = []
for i in range(5):
    num = int(input(f"Enter the {i + 1} number: "))
    nums.append(num)

print(nums)

s = sum(nums)
m = max(nums)
mi = min(nums)
c = len(nums)
avg = s / c
print("sum: ", s)
print("max: ", m)
print("min: ", mi)
print("len: ", c)
print("average: ", avg)


uniqueNumbers = list(set(nums))
print(uniqueNumbers)