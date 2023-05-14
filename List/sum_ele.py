a = []
n = int(input("Enter the value of n:"))
print("Enter the values into list...")
for i in range(n):
    data = int(input())
    a.append(data)
print("After adding data's:",a)
sm = 0
for i in range(n):
    sm = sm + a[i]
print("Sum of all elements:",sm)    