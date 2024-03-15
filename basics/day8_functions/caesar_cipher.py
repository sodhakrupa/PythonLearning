from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
run_caeser = "yes"
def caeser(text, shift, direction):
    caeser_text = ""
    for char in text:
        if char.isalpha():
            index=alphabet.index(char)
            shifted_index = 0
            if direction == "encode":
                shifted_index = index + shift
                if shifted_index >= len(alphabet):
                    shifted_index = shifted_index - len(alphabet)
            elif direction == "decode":
                shifted_index = index - shift
                if shifted_index < 0:
                    shifted_index = len(alphabet) - shifted_index
            caeser_char = alphabet[shifted_index]
        else:
            caeser_char = char
        caeser_text += caeser_char
    print(f"caeser text is {caeser_text}")

while run_caeser == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift >= len(alphabet):
        shift = shift % (len(alphabet)-1)
    caeser(text, shift, direction)
    run_caeser =input("Type 'yes' if you want to go again. Otherwise type 'no'.")

