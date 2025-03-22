currency=input("Enter your currency(USD/JPY/GBP/EURO/RUB):").upper()
amount=float(input("Enter your amount:"))
if currency=='USD':
    to_inr=amount*86.63
elif currency=='JPY':
    to_inr=amount*0.58
elif currency=='GBP':
    to_inr=amount*112.64
elif currency=='EURO':
    to_inr=amount*94.82
elif currency=='RUB':
    to_inr=amouont*1.06
else:
    print("Invalid Currency")
print(f"{amount}{currency} is {round(to_inr,2)INR")
    
