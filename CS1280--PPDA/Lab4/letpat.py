a=65
c=66
for i in range(4):
       for j in range(a,c):
             print(chr(j),end="")
       c+=2
       print("\n")
c-=4
for i in range(3):
       for j in range(a,c):
             print(chr(j),end="")
       c-=2
       print("\n")
