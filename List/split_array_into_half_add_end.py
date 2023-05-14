a = []
n = int(input("Enter the value of n:"))
for i in range(n):
    data = int(input())
    a.append(data)
k = int(input("Enter the split value:"))
a = a[k:] + a[0:k] 
print("After splitting the list:",a)  