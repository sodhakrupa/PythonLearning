import random

coin_side = random.randint(0,1)
if coin_side == 0:
    print("Heads")
elif coin_side == 1:
    print("Tails")
else:
    print("Invalid coin side")
