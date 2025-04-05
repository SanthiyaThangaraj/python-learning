transform_data=[]
n=int(input("Enter range:"))
for i in range(n):
    a=int(input("Enter number:"))
    
    transform_data.append(a)

#filter out all negative numbers using filter()
fil=list(filter(lambda x: x<0, transform_data))
print(fil)
    
#square each remaining number using map()
squ=list(map(lambda x:x**2, transform_data))
print(squ)

#calculate the product of all resulting values using functools.reduce()
from functools import reduce
combined_list=fil+squ
pro=reduce(lambda x,y: x*y, combined_list
           )
print(pro)

