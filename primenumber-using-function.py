def check_prime(num):
    if num<2:
        print("This is not a prime number")
    elif num>2:
        for i in range(2,num):
            if num%i==0:
                print("This is not a prime number")
                return
        print("This is a prime number")

num=int(input("Enter a number: "))
check_prime(num)
