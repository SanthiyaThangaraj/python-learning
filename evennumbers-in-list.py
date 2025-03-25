#Write Python code to create a new list containing only the even numbers from the original list data = [10, 21, 32, 43, 54, 65, 76]
udata=[10,21,32,43,54,65,76]
print(udata[::2])

#another method like
for x in udata:
    if(x%2==0):
        print(x)
