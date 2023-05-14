a = []
n = int(input("Enter the value of n:"))
print("Enter the values into list:")
for i in range(n):
    data = int(input())
    a.append(data)
print("Elements of list:",a)
a.sort()
print("Second smallest element:",a[1])    