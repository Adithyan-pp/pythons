arr=[2,3,4,5,6,7]

square_num=[num**2 for num in arr]

print(square_num)
# 
add_ten=[num+10 for num in arr]

print(add_ten)

odd_numbers=[num for num in arr if num%2!=0]

print(odd_numbers)


even_numbers=[num for num in arr if num%2==0]
print(even_numbers)

num_gt_five=[num for num in arr if num>5]
print(num_gt_five)
#
text=["apple","iphone","orange","potatto","tomatto"]

vowel_words=[w for w in text if w[0]in ['a','e','i','o','u']]

print(vowel_words)

consonant_words=[w for w in text if w[0]not in ['a','e','i','o','u']]

print(consonant_words)
# longest words

long=max([len(w) for w in text])

longest_words=[w for w in text if len(w)==long]

print(longest_words)

