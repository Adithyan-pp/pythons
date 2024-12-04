words=["hello","hai","hello","this","is","this","is","hello"]

words_frequency={w:words.count(w)for w in words}

print(words_frequency)

recursive_words=[k for  k,v in words_frequency.items()if v>1]

print(recursive_words)

#display non_recursive_words

non_recursive=[]