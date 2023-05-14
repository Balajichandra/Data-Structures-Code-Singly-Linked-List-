s = str(input("Enter the string:"))
str_len = 0
for i in s:
    if i != ' ':
        str_len+=1
print("Length of string:",str_len)    