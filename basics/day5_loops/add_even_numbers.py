number = int(input("Enter number between 0 to 1000\n"))
sum = 0
for n in range(0, number+1):
    if n%2 ==0:
        sum +=n
print(f"Sum is {sum}")