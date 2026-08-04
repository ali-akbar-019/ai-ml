nums = [1, 2,3 ,4 ,5]

# append

nums.append(10)
print(nums)

# insert pos and data
nums.insert(1, 12)
print(nums)


# extend
a = [1, 2]
b = [3, 4]
a.extend(b)
# extends adds one list to the other
print(a)


# removing
nums = [1,2,3,4,5,6]
nums.remove(2)
print(nums)

# pop , remove by index
print(nums.pop(2))
print(nums)

# clear -> clear the list

# nums.clear()
# print(nums)

# searching
print(20 in nums)



# useful method
# count
print(nums.count(1))


# index()
print(nums.index(1))

# sort
print(nums.sort())

print(nums)


# reverse
nums.reverse()
print(nums)





# looping throug the list 
for i in nums:
    print(i)
    


# max , min,  count, len, sum
