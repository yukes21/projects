print("Welcome to the tip calculator.")
total_bill=float(input("What is the total bill? $"))
tip=int(input(f"What percentage tip would you like to give? 10, 12, or 15?"))
a= tip/100
per= a*total_bill + total_bill
split=int(input(f"How many people to split the bill?"))
div=per/split
f=round(div, 2)
f="{:.2f}".format(div)
print(f"Each person should pay: ${f}")


