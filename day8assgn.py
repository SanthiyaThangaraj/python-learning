#create a list of even numbersfrom 0 to 200
#method1
num=list(range(201))
even_numbers=num[::2]
print(even_numbers)

#method2
mynum=[]
for num in range(200):
    mynum.append(num)

print(mynum[::2])

#celsius to fahrenheit
celsius=float(input("Enter degree: "))
print(f"conversion: {celsius*1.8+32}")
