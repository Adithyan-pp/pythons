read_path="C:\\Users\\adith\\OneDrive\\Desktop\\Pythonworks\\data_set\\words.txt"

write_path="C:\\Users\\adith\\OneDrive\\Desktop\\Pythonworks\\data_set\\palindrome.txt"

f_read=open(read_path)

f_write=open(write_path,"w")

for line in f_read:

    word=line.rstrip("\n")

    reversed_word=word[::-1]

    if word==reversed_word:

        f_write.write(word+"\n")

f_read.close()

f_write.close()

