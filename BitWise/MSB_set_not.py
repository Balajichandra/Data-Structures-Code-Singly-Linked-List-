n = int(input("Enter the value of n:"))
if ( n & (1<<31) != 0):
    print("MSB is set")
else:
    print("MSB is not set")    