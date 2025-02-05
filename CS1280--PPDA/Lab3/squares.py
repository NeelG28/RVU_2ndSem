import time,sys
start=time.time()
squares=[x**2 for x in range(1,1000001)]
end=time.time()
print("list comprehension time : ",end-start)
print(sys.getsizeof(squares))
#using traditional for loop
start=time.time()
squares=[]
for x in range(1,1000001):
     squares.append(x**2)
end=time.time()
print("for loop time : ",end-start)
print(sys.getsizeof(squares))
