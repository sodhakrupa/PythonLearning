print("Welcome to tip calculator!!\n")
bill= float(input("Total Bill?"))
tip = int(input("tip? 10,12 or 15%"))
person = int(input("No of persons?"))
result =  (bill + bill * tip / 100)/person
print(f"Each person has to pay {result}")