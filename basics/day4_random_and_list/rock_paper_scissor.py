import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock,paper,scissors]
print("Lets play Rock~Paper~Scissor\n")
user_choice = int(input("Choose 0 for Rock, 1 for paper, 2 for Scissor\n"))

if user_choice not in [0,1,2]:
    print("Invalid choice, Please choose from 0, 1 or 2")
    exit()

print(game_images[user_choice])
computer_choice = random.randint(0,2)
print(f"Computer chose {game_images[computer_choice]}")
if user_choice == computer_choice:
    print("Its a draw")
elif user_choice == 0 and computer_choice == 2:
    print("You Win")
elif user_choice == 2 and computer_choice == 0:
    print("You Lose")
elif user_choice > computer_choice:
    print("You Win")
elif computer_choice > user_choice:
    print("You Lose")

