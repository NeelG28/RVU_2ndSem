num=int(input("Enter no. of digits : "))
print("Enter the numbers :")
a=[]
sum=0
avg=0.00
for i in range(num):
     n=int(input())
     a.append(n)
for i in range(num):
     sum=sum+a[i]
avg=float(sum/num)
print(f"The average of numbers in the array is {avg}")
