n = int(input("Enter the value of n:"))
zero_cnt,one_cnt=0,0
for i in range(0,32):
    if((n>>i & 1)== 1):
        one_cnt+=1
    else:
        zero_cnt+=1
print("Total number of ones:",one_cnt) 
print("Total number of zeros:",zero_cnt)           