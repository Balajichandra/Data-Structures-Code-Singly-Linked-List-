n = int(input("Enter the value of n:"))
res = (n & 0x0f)<<4 | (n & 0xf0)>>4
print("After swapping nibbles:",res)