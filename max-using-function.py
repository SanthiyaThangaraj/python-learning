#write a function called max_of_three that returns the maximum of three numbers
def max_of_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

a=int(input("Enter a :"))
b=int(input("Enter b :"))
c=int(input("Enter c :"))
print (max_of_three(a,b,c))
