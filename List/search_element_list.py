a = []
n = int(input("Enter the value of n:"))
print("Enter the elements into list...")
for i in range(n):
    data = int(input())
    a.append(data)
print("Elements of list:",a)
ele_src = int(input("Enter the element to be searched:"))
for i in range(n):
    if a[i] == ele_src:
        index = i
        flag = True
        break
    else:
        flag = False        
if flag == True:
    print("The given element is present in index:",index)
else:
    print("Sorry no element is present")    