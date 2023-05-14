a,b,c=[],[],[]
n=int(input("Enter the value of n for list A:"))
print("Enter the values into list A...")
for i in range(n):
    data_A = int(input())
    a.append(data_A)
print("ELements of list A:",a) 
m=int(input("Enter the value of n for list B:"))
print("Enter the values into list B...")
for i in range(m):
    data_B = int(input())
    b.append(data_B)
print("ELements of list A:",b)
c = a + b
c.sort()
print("Merged and sorted list:",c)    