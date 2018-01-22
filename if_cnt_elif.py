i=1
n=int(input("Enter no:"))
while 1:
    i=i+1
    if(i<=n//2):
        print("Continue",i)
        continue
    elif(i<=n):
        print(i)
        break
input("Press ENTER to EXIT")
