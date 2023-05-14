a,b=[],[]
n = int(input("Enter the value of n:"))
print("Enter the elements into list...")
for i in range(n):
    data = int(input(""))
    a.append(data)
print("Elements of list A:",a)
m = int(input("Enter the value of m:"))
print("Enter the elements into list...")
for i in range(m):
    data_B = int(input(""))
    b.append(data_B)
print("Elements of list B:",b) 
print("Union of two list:",list(set().union(a,b)))