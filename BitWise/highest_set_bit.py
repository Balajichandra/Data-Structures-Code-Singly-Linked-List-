n = int(input("Enter the value of n:"))
for i in range(32):
    if((n>>i) & 1):
        flag = i
print("Highest set bit:",flag)        