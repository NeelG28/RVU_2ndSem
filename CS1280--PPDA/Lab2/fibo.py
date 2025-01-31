n1=0
n2=1
t=0
print("First 10 terms of the fibonacci series : ")
print(f"{n1},{n2}",end=" ")
for i in range(2,10):
         t=n1+n2
         print(t,end=", ")
         n1=n2
         n2=t
