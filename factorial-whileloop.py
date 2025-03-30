#write a program using a while loop to find the factorial of a number provided by the user
num=int(input("Enter number: "))
temp=1
while num!=0:
    temp=temp*num
    num-=1
print(temp)
    
