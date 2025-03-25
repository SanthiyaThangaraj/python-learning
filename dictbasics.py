dict={'name':'sandy','age':int(input()),'gender':'f'}
print(dict)
print(dict['age'])
dict['name']='puppy'
print(dict)
dict.update({'name':'sandy','gender':'m'})
print(dict)
dict.popitem()
print(dict)
del dict
print(dict)

dict1=[{'name':'sandy','age':'32'},
       {'name':'puppy','age':'42'},
       {'name':'bag','age':'22'}]
print(dict1)
print(dict1[1]['name'])
dict1[1]['name']='dadda'
print(dict1)
print(dict1[0])
dict1.append({'gender':'f'})
print(dict1)
