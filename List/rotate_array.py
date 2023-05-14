a = []
n = int(input("Enter the value of n:"))
print("Enter the elements into list...")
for i in range(n):
    data = int(input())
    a.append(data)
print("Elements of list:",a)
rotate = int(input("Enter the number of rotations:"))
a = a[-rotate:]+a[0:rotate+1] 
print("After rotating the array:",a)   