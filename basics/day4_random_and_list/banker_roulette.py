import random

names_string = input("Enter names comma separated.\n")
names = names_string.split(',')
random_index = random.randint(0, len(names)-1)
print("Bill will be paid by person "+names[random_index])
