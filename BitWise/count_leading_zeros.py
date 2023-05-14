n = int(input("Enter the value of n:"))
cnt = 0
for i in range(32):
    if((n<<i) & (1<<31)):
        break 
    cnt+=1
print("Total number of leading zeros:",cnt)    