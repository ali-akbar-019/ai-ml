A = {1,2,3,4,5}
B = {4,5,6,7}
print("union: ", A | B)
print("intersection: ", A & B)
print("A - B: ", A - B)
print("B - A: ", B - A)
print("Symmetric difference: ", A ^ B)


print("Intersection Update")
A.intersection_update(B)
print(A)
print("Intersection Update")
A.difference_update(B)
print(A)
print("Intersection Update")
A.symmetric_difference_update(B)
print(A)