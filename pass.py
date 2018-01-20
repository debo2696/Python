for i in range(0,5):
    j=5
    ps=str(input("Enter the password:"))    
    if(ps=="debo2696"):
        print("Welcome to ur TERMINAL:")
        break
    else:
        if((j-i-1)==0):
            print("Try again later")
            break
        elif((j-i-1)==1):
            print("You are left with", (j-i-1),"more attempt")
        elif((j-i-1)!=1):
            print("You are left with", (j-i-1),"more attempts")
