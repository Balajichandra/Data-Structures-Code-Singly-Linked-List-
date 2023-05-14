vowels = ['a','e','i','o','u','A','E','I','O','U']
s = str(input("Enter the string:"))
vowel_cnt=0
for i in s:
    if i in vowels:
        vowel_cnt+=1
print("Total number of vowels:",vowel_cnt)        