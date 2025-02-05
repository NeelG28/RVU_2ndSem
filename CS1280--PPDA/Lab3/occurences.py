num=int(input("Enter the number of names : "))
print("Enter the names :")
a=[]
count=0
for i in range(num):
     n=input()
     st=n.lower()
     a.append(st)
       
for name in a:
     for char in name:
         if char=='a':
             count+=1
print(f"The number of occurences of 'a' is : {count}")
