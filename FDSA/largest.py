a=[10,20,30]
max=0
min=a[-1]
for i in range(0,3):
    if a[i]>max:
        max=a[i]
    if a[i]<min:
        min=a[i]
print(f"{max} and {min}")

