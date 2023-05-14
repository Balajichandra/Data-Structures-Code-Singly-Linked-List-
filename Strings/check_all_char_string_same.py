# Q WAP to find if all the characters of a string are same
s = str(input("Enter the string:"))
for i in range(1,len(s)):
    if s[i] != s[0]:
        flag = False
    else:
        flag = True
if flag == True:
    print("All the characters are same...")
else:
    print("Not all charactrs are same...")                 