def add(p,q):
      return p+q
def sub(p,q):
      return p-q
def pro(p,q):
      return p*q
def div(p,q):
      return p/q
      
print("Enter the operation to be performed : ")
print("a. Sum")
print("s. Difference")
print("m. Product")
print("d. Quotient")

choice=input("Enter choice a/s/m/d : ")
var1=int(input("Enter the first number : "))
var2=int(input("Enter the second number : "))

if(choice=='a'):
        fs=add(var1,var2)
        
if(choice=='s'):
        fs=sub(var1,var2)

if(choice=='m'):
        fs=pro(var1,var2)

if(choice=='d'):
        fs=div(var1,var2)

print(fs)
        

