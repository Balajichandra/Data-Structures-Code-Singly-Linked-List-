s = str(input("Enter the string:"))
words_cnt = 1
char_cnt = 0
for i in s:
    char_cnt+=1
    if i == ' ':
        words_cnt+=1
        char_cnt-=1   
print("Total number of words:",words_cnt)
print("Total number of characters:",char_cnt)        
        