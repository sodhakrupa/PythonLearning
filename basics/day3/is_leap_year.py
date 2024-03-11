# if year is divisible by 4
# except year is also divisible by 100 unless it is divisible by 400
# eg 2000 is leap year - divisible by 4,not divisible by 100 but also divisible by 400
# eg 2100 is leap year - divisible by 4, divisible by 100 , not divisible by 400

year = int(input("Enter year to check if it is a leap year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

