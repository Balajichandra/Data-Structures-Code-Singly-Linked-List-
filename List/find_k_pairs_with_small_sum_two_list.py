a,b=[],[]
n = int(input("Enter the value of n:"))
for i in range(n):
    c = int(input())
    a.append(c)
m = int(input("Enter the value of m:"))
for j in range(m):
    d = int(input())
    b.append(d)
k = int(input("Enter the k value:"))
for i in range(n):
    for j in range(m):
        if (a[i]+b[j] == k):
            print("Pair found:",{a[i],b[j]})
        else:
            continue           