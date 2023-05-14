s = str(input("Enter the numbers:"))
n = len(s)
i = 0
flag = False
while (i <n and s[i] == '0'):
    i = i+1
print(i)    
while (i<n):
    if(s[i] == '0'):
        flag = True
    i+=1
if flag == True:
    print("Given number string is duck number...")
else:
    print("Given number is not a duck number")    