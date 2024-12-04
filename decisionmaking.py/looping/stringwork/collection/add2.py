colours={"red","green","blue"}

colours.add("yellow")

print(colours)
#
arr=[10,10,20,30,40,50,40]

st=set()

for num in arr:

    st.add(num)

print(st)
#
st1={10,20,30,40,50}

st1.remove(50)

print(st1)

st2={10,20,60,70,80}

intersection_set=st1.intersection(st2)
#
union_set=st1.union(st2)

print(union_set)
#
difference_set=st1.difference(st2)

difference_set=st1.difference(st2)

print(difference_set)