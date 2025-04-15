#Create a nested function where the inner function modifies a variable from the outer function using nonlocal

def water():
    water_count=0
    def drink():
        nonlocal water_count
        water_count+=1
        return water_count
    return drink()

print(water())

#Write a program that uses a built-in function and also defines a variable with the same name.

data=[1,4,3,6,8]
print(max(data))
max=45
print(max)

#Modify a global list inside a function using the global keyword.

data=10
def laptop():
    global data
    data+=1
    return data

print(laptop())
