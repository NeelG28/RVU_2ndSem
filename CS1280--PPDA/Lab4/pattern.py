n=int(input("Enter number of lines in pattern : "))
sp=n-1
for i in range(1,n+1):
      print(" "*sp,end="")
      for j in range(i):
            print("*",end=" ")
      sp-=1
      print()
