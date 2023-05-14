a = []
n = int(input("Enter the value of n:"))
print("Enter the values into list...")
for i in range(n):
    data = int(input())
    a.append(data)
print("Elements of list:",a)
odd,even = [],[]
for i in range(n):
    if a[i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])
print("Elements of odd list:",odd)
print("Elements of even list:",even)                