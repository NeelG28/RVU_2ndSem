def digits(n,a):
    if n==0:
        return a
    else:
        
        return digits(n//10,a+n%10)
n=int(input("Enter a number : "))
res=digits(n,0)
print(f"The sum of digits in the number {n} is {res}")
        

