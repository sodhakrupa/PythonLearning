import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for letter in chosen_word:
    display.append("_")

print(display)

while display.count("_") > 0:
    guess = input("Guess a letter: ").lower()
    #Replace guessed letter
    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess

    print(display)

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)