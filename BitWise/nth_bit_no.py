n = int(input("Enter the value of n:"))
bp = int(input("Enter the bit-position:"))
res = n>>bp & 1
print("Position of bit:",res)