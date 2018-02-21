import time
print("Enter range:")
r=int(input())
for i in range(1,r,1):
    print(i,":",time.asctime())
