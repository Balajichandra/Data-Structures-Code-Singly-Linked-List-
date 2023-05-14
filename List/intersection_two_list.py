a,b = [],[]
n = int(input("Enter the value of n:"))
print("Enter the elements into list_A...")
for i in range(n):
    data = int(input())
    a.append(data)
print("Elements of list_A:",a)
m = int(input("Enter the value of m:"))
print("Enter the elements into list_B...")
for i in range(m):
    data_b = int(input()) 
    b.append(data_b)
print("Elements of list_B:",b)       
print("Intersection of two list:",list(set(a)&set(b)))