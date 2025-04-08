#create a function that searches a string or the character 'x', uses break when found, and returns the position or -1 if not found.
def search(val):
    for char in val:
        if char=='x':
            break
        return val[-1]

val='expire'
print(search(val))
    
