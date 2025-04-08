#write a function that processes a list of values but immediately returns False if any value is zero.
def process(val):
    for i in range(len(val)):
        if val[i]==0:
            return False
        print(val[i])

val=[3,2,5,0,9]
print(process(val))
