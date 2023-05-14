n = int(input("Enter the value of n:"))
if( n & (1<<31)):
    print("The given number is negative")
else:
    print("The given number is positive")    