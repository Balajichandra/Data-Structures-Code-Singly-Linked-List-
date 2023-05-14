a = []
n = int(input("Enter the value of n:"))
for i in range(n):
    b = int(input())
    a.append(b)
print("Elements of list:",a) 
a.sort()
print("Largset element in list:",a[n-1])   