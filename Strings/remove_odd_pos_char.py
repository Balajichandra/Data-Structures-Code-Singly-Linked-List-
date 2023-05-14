s = str(input("Enter the string:"))
res = ""
for i in range(len(s)):
    if i % 2 == 0:
        res = res + s[i]
print("After removing odd chars:",res)        