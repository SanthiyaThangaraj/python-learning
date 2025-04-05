#write a lambda function that returnsa function to calculate x^n, where n is given at runtim
power=lambda x,n:x**n
x=int(input("Enter value for x:"))
n=int(input("Enter value for n:"))
print(power(x,n))

