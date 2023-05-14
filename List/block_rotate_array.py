a = []
n = int(input("Enter the value of n:"))
print("Enter the elements in list...")
for i in range(n):
    data = int(input())
    a.append(data)
print("Elements of list_A:",a)
rotate = int(input("Enter the times to rotate:"))
a = a[rotate:]+a[0:rotate]
print(a)    