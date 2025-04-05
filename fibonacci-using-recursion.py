def fibonacci(n):
    if (n==0):
        return n
    elif (n==1):
        return n
    else:
        return fibonacci(n-2)+fibonacci(n-1)

n=int(input("Enter range:"))
for i in range(n):
    print(fibonacci(i
                    ))        
