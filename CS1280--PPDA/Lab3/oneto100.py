num=int(input("Enter no. of digits : "))
print("Enter the numbers :")
a=[]
sum=0
avg=0.00
for i in range(num):
     n=int(input())
     a.append(n)
fa=[]
for x in a:
     if 1<=x<=100:
          fa.append(x)
print(f"The newlist containing only numbers between 1 and 100 : {fa}")
