string1 = "ace"
string2 = "abcde"
ptr = 0
is_subsequence = True
for char in string1:
    while ptr < len(string2) and string2[ptr] != char:
        ptr +=1
    if ptr == len(string2):
        is_subsequence = False
        break
    ptr += 1
print(is_subsequence)