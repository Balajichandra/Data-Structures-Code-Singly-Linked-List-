n = int(input("Enter the value of n:"))
for i in range(32):
    if ((n>>i) & 1):
        flag = i
        break
print("The lowest set bit:",flag)    