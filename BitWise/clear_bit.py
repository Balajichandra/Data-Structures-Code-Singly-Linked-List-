n = int(input("Enter the value of n:"))
bp = int(input("Enter the bit position:"))
res = n & ~(1<<bp)
print("After clearing the bit:",res)