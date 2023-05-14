a,b = int(input("Enter the value of a:")),int(input("Enter the value of b:"))
a = a ^ b
b = a ^ b
a = a ^ b
print("After swapping:",a,b)