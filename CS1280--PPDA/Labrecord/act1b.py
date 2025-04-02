def temperature_converter():
    print("Temperature Converter")
    temp=float(input("Enter temperature : "))
    print("Convert to : ")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Fahrenheit to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Celsius to Kelvin")
    print("6. Kelvin to Fahrenheit")
    choice=input("Enter choice (1/2/3/4/5/6) : ")
    if choice=='1':
        fahrenheit=(temp*9/5)+32
        print(f"{temp} C is {fahrenheit} F")
    elif choice=='2':
        celsius=(temp-32)*5/9
        print(f"{temp} F is {celsius} C")
    elif choice=='3':
        kelvin=(5/9*(temp-32))+273
        print(f"{temp} F is {kelvin} K")
    elif choice=='4':
        celsius=temp-273
        print(f"{temp} K is {celsius} C")
    elif choice=='5':
        kelvin=temp+273
        print(f"{temp} C is {kelvin} K")
    elif choice=='6':
        fahrenheit=(9/5*(temp-273))+32
        print(f"{temp} K is {fahrenheit} F")
    else:
        print("Invalid input")

temperature_converter()
    
