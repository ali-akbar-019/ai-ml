st = set([3,2,3,3])
print(st)

st.add(50)
print(st)
# add multiple elements
st.update([60,20,80])
print(st)
# remove 20
st.remove(20)
print(st)

# ye agar el exist na kare tehn kch nahi kehta rmeove error deta ha 
st.discard(100)
print(st)

st.pop()
print(st)

st.clear()
print(st)

st = {1,3,4,5,6,7,211}
st2 = st.copy()
# cs sets are mutable thats why copy use karo else same locaiton ko point kare ge
print("st1 : ", st, " st2: ", st2)




