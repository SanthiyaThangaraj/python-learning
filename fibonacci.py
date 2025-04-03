#write a function fibonaacci(n)that returns the nth fiboncci number using recursion
def fibonacci(num):
    n1=0
    n2=1
    print("Fibonacci series:",n1,n2, end=" ")
    for i in range(2,num):
        n3=n1+n2
        n1=n2
        n2=n3
        
        print(n3, end=" ")

num=int(input("Enter range:"))
fibonacci(num)
