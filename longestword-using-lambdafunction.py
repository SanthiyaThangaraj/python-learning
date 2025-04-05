#use a lambda function with reduce() to find the longest word in a list of strings
from functools import reduce
a=['python','programming','class','studying','mobilephones']
large_word= reduce(lambda x,y:x if len(x)>len(y) else y,a)
print(large_word)
