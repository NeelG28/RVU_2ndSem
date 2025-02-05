num=int(input("Enter no. of digits : "))
print("Enter the numbers :")
a=[]
sum=0
for i in range(num):
     n=int(input())
     a.append(n)
for i in range(num):
     sum=sum+a[i]
print(f"The sum of numbers in the array is {sum}")
