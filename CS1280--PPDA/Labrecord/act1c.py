def find_largest():
    print("Find the largest of three numbers")
    num1=float(input("Enter first number : "))
    num2=float(input("Enter second number : "))
    num3=float(input("Enter third number : "))
    num4=float(input("Enter fourth number : "))
    num5=float(input("Enter fifth number : "))
    
    largest=num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    if num4 > largest:
        largest = num4
    if num5 > largest:
        largest = num5
    
    print(f"The largest number is : {largest}")

find_largest()
