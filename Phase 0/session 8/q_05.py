st = set()
for i in range(10):
    num = int(input("Enter a number: "))
    st.add(num)

print("all the unique numbers added by the users are ")
print(st)
# 
all_students = {"Ali","Ahmed","Sara","Usman","Ayesha"}
present = {"Ali","Sara","Usman"}
print(present)
print(all_students - present)
print(all_students)