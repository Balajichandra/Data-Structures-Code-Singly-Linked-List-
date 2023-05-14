a = []
n = int(input("Enter the value of n:"))
print("Enter the elements into array...")
for i in range(n):
    data = int(input())
    a.append(data)
print("Elements of list:",a)
a = a[::-1] 
print("After reversing the array:",a)   