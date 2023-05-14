a = []
n = int(input("Enter the value of n:"))
print("Enter the elements into list")
for i in range(n):
    data = int(input())
    a.append(data)
print("After adding data's:",a)
a.sort()
print("Second largest element:",a[-2])    