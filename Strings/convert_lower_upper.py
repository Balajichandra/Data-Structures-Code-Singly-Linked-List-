s = str(input("Enter the string:"))
for i in s:
    if s[i] >= 'a' and s[i] <= 'z':
        s[i] = s[i] -32
print(s)        