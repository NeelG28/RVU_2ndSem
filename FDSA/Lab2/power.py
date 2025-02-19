def power(base,exp):
    if exp==1:
        return base
    elif exp==0:
        return 1
    else:
        return base*power(base,exp-1)
n=int(input("Enter the base number : "))
e=int(input("Enter the exponent number : "))
res=power(n,e)
print(res)
