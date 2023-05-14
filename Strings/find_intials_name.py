s = str(input("Enter the string:"))
if len(s) == 0:
    print("Sorry no string...")
words = s.split(" ")
for word in words:
    print(word[0].upper(),end=' ')
        