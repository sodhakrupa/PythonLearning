#For Love Scores less than 10 or greater than 90, the message should be:
#"Your score is *x*, you go together like coke and mentos."

#For Love Scores between 40 and 50, the message should be:
#"Your score is *y*, you are alright together."

#Otherwise, the message will just be their score. e.g.:
#"Your score is *z*."

print("The Love Calculator is calculating your score...")
name1 = input("What is your name?").lower()
name2 = input("What is their name?").lower()
combined_name = name2 + name1

letter_t = combined_name.count("t")
letter_r = combined_name.count("r")
letter_u = combined_name.count("u")
letter_e = combined_name.count("e")

first_digit = str(letter_t + letter_r + letter_u + letter_e)

letter_l = combined_name.count("l")
letter_o = combined_name.count("o")
letter_v = combined_name.count("v")
letter_ee = combined_name.count("e")

second_digit = str(letter_l + letter_o + letter_v + letter_ee)

score = int(first_digit + second_digit)

if score <10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score < 40 and score > 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")