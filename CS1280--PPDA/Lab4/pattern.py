n=int(input("Enter number of lines in pattern : "))
sp=n-1
c=1
for i in range(n):
      print("  "*sp,end="")
      for j in range(c):
            print("*",end=" ")
      sp-=1
      c+=2
      print()
