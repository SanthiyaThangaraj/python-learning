#Remove all duplicates from a list without using set()

data=[1,3,6,3,9,1,5]
data=list(dict.fromkeys(data))
print(data)
    
