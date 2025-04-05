#write a lambda function to check if a given year is a leap year.(Hint: A uear is a leap uear if it is divisibke by 4 and not by 100 unless also divisible by 400)
leap= lambda x: f"{x} is a leap year" if (x%4==0 and  (x%100!=0 or (x%400==0))) else f"{x} is not a leap year"
x=int(input("Enter year:"))
print(leap(x))
