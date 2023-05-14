a = []
n = int(input("Enter the value of n:"))
print("Enter the elements into list...")
for i in range(n):
    data = int(input())
    a.append(data)
print("Elements of list:",a) 
sum_val = int(input("Enter the summation value to be found:"))
val_a,val_b=0,0
for i in range(0,n):
    for j in range(i+1,n):
        if (a[i] + a[j]) == sum_val:
            val_a,val_b=a[i],a[j]
            break
        else:
            continue
if val_a != 0 and val_b != 0:
    print("The pair of values found:",val_a,val_b)
else:
    print("Sorry no value found...")                
