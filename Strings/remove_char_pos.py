s = str(input("Enter the string:"))
pos = int(input("ENter the position to be remove:"))
res = s[:pos] + s[pos+1:]
print("After removing char:",res)