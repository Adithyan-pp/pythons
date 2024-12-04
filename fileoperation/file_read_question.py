f=open("C:\\Users\\adith\\OneDrive\\Desktop\\Pythonworks\\data_set\\question.txt")

words=[]

for line in f:

    line=line.rstrip("\n")

    all_words=line.split(" ")

    for w in all_words:

        words.append(w)


word_count={w:words.count(w)for w in words}



nested_word_count=[[v,k] for v,k in word_count.items()]

print(sorted(nested_word_count,reverse=True))