'''Write a function called data_analyzer that processes a list of numeric values and returns a dictionary with the following information:

    -> The sum of all values (using the appropriate built-in function)
    -> The minimum and maximum values (using appropriate built-in functions)
    -> The average (mean) of all values (calculate this using built-in functions)
    -> The number of values that are above the average
    -> A sorted version of the original list (using the appropriate built-in function)'''
def data_analyzer(values):
    total=sum(values)
    minimum=min(values)
    maximum=max(values)
    avg=sum(values)//len(values)
    for i in values:
        temp=0
        if i>avg:
            temp+=1

    avg_values=temp
    sort=sorted(values)
    dic_values={"sum": total,
                "minimum value": minimum,
                "maximum value":maximum,
                "average of all values": avg,
                "no of values are above the average": avg_values,
                "sorted version": sort}
    print(dic_values)

values=[63,53,64,95,43,87]
print(values)
data_analyzer(values)

            
    
