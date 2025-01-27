a=int(input("Enter a number : "))
c=0
for i in range(1,a):
        if a%i==0:
              c=c+1
if c>1:
     print("The number is not prime")
else:
     print("The number is prime")
