# merge and sort
l1 = [1,2,3,4,5]
l2 = [2,3,4,5,6]
l3 = l1 + l2
l3 = sorted(l3)
l3 = list(set(l3))
print(l1)
print(l2)
print(l3)

# find the second largest
maxi = max(l3)

mini = max([x for x in l3 if x != maxi])
print(maxi, mini)

# 1. Move zeros to end
arr = [0,1,0,3,12]
arr = [x for x in arr if x != 0] + [0] * arr.count(0)
# [1,3,12,0,0]

# 2. Rotate right by 1
arr = [1,2,3,4,5]
arr = [arr[-1]] + arr[:-1]
# [5,1,2,3,4]

# 3. Check if sorted ascending
arr = [1,2,3,4,5]
is_sorted = arr == sorted(arr)
# or
is_sorted = all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
# True