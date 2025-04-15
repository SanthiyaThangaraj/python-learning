#Count the number of even and odd numbers in a list

list1=[1,4,8,5,2,7,9]
e_count=0
o_count=0
for item in list1:
    if item %2==0:
        e_count+=1
    else:
        o_count+=1

print(e_count)
print(o_count)
        
