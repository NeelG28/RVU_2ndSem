num=int(input("Enter a number : "))
newnum=0
dig=0
temp=num
while temp!=0:
      dig=temp%10
      newnum=(newnum*10)+dig
      temp=temp//10
print(f"The new number after reversing is {newnum}")
