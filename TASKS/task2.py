word1="ab"

word2="pqrs"

result=""
smallest=word1 if len(word1)<len(word2) else word2

largest=word1 if len(word1)>len(word2) else word2

for i in range(0,len(smallest)):
    result+=word1[i]+word2[i]
balance_word=largest[len(smallest):]

result+=balance_word

print(result)