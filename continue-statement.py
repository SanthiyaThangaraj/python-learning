#create a function that counts non-space characters in a string but uses continue to skip vowels.

def counts(val):
    count=0
    vowels=['a','e','i','o','u','A','E','I','O','U']
    for char in val:
        if char in vowels:
            continue
        if char!=' ':
                count+=1                
    return count
            

val='apple mango'
print(counts(val))
                
