#Based on a user's order, work out their final bill.
#Small pizza (S): $15
#Medium pizza (M): $20
#Large pizza (L): $25
#Add pepperoni for small pizza (Y or N): +$2
#Add pepperoni for medium or large pizza (Y or N): +$3
#Add extra cheese for any size pizza (Y or N): +$1

print("Welcome to Pizzeria!!")
size = input("What pizza size you need?S, M, L\n")
add_pepperoni = input("Do you want to add Pepperoni? Y or N\n")
add_cheese = input("Do you want to add extra cheese?\n")
bill=0
if size == "S" or size == 's':
    bill = 15
elif size == "M" or size == 'm':
    bill = 20
elif size == "L" or size == 'l':
    bill = 25

if add_pepperoni == "Y" or add_pepperoni == "y":
    if size == "S" or size == 's':
        bill +=2
    else:
        bill +=3

if add_cheese == "Y" or add_cheese == "y":
    bill+=1
print(f"Your bill is {bill}")