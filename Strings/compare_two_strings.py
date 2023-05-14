s1 = str(input("Enter the String1:"))
s2 = str(input("Enter the String2:"))
for i in s1:
    for j in s2:
        if i == j:
            flag = True
        else:
            flag = False 
if flag == True:
    print("Two strings are same...")
else:
    print("Two Strings are not same...")                   