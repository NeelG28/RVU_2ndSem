n=int(input("Enter length "))
c=n-1
ran=1
for i in range(n): 
        print(" "*c,end="")
        for j in range(ran):
              print("*",end="")
        print("\n")
        c=c-1
        ran=ran+2

