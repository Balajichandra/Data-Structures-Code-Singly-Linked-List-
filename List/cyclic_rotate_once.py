a = []
n = int(input("Enter the value of n:"))
print("Enter the elements into list...")
for i in range(n):
    data = int(input())
    a.append(data)
print("Elements of list:",a)
a = a[-1:]+a[0:n-1] 
print("After cyclic rotation of list by once:",a)   
