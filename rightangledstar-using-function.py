#create a functionn called print_pattern that takes an integer n and prints a right-angled triangle pattern of stars with n rows
def print_pattern(n):
    for i in range(1,n+1):
        print()
        for j in range(1,i+1):
            print("*", end=" ")

n=int(input("ENTER N :"))
print_pattern(n)


