n=int(input("Enter a number : "))
t=n
rev=0
while t!=0:
        r=t%10
        rev=rev*10+r
        t=t//10
print(f"Reverse of number {n} is {rev}")
