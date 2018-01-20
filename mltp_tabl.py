n=int(input("Enter the no. of multiplication table u want to see:"))
y=int(input("How much should the table range to?:")) 
for i in range(1,(n+1),1):
    print("\n")
    for j in range(1,(y+1),1):
        print(i,"x",j,"=",(i*j))
          
            
