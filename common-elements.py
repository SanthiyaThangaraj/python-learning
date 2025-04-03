#write a funcion find_common_elements (list1,list2) that returns a list of common elements between two lists
n=int(input("Enter the list1 size:"))
list1=[]
list2=[]
for i in range(n):
    x=int(input())
    list1.append(x)
print(list1)
m=int(input("Enter the list2 size:"))
for i in range(m):
    x=int(input())
    list2.append(x)
print(list2)
newlist=[]
def common_elements(list1,list2):
    for i in list1:
        for j in list2:
            if i==j:
                newlist.append(i)
common_elements(list1,list2)
print("Common elements among two list:",newlist)
