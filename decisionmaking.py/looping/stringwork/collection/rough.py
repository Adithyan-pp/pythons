users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]

rahul_followers=["rohit","kohli","rishab","rahul"]

sanju_followes=["sanju","rohit","kohli"]

common_followers=set(rahul_followers).intersection(set(sanju_followes))

rahul_follow_suggestion=set(users).difference(set(rahul_followers))

print(rahul_follow_suggestion)

print(common_followers)

#
st1={1,2,3,10,20}
st2={1,2,3,4,5}

symetric_difference=st1.symmetric_difference(st2)

print(symetric_difference)

st1.update(st2)

print(st1)
#
text="this is a text to remove duplicate words this text is simple"
#
text2="this simple text remove duplicate words"



words=text.split(" ")

print(set(words))