# Simple tool to run all possible shifts on a cipher text given some alphabet
# https://github.com/dimike96

# Needed imports
import string

# Defining alphabets
english_alphabet_lower = string.ascii_lowercase
english_alphabet_upper = string.ascii_uppercase
digits = string.digits
all_chars = string.printable

common_alphabets = [english_alphabet_lower, english_alphabet_upper, digits, all_chars]


# Run through all shifts for alphanumeric texts, shifting characters and digits separately
def brute_shift_alphanumerics(text):
    shifted_texts = []
    for char in text:
        if char in english_alphabet_lower:
            char_alpha = english_alphabet_lower
        elif char in english_alphabet_upper:
            char_alpha = english_alphabet_upper
        elif char in digits:
            char_alpha = digits
        for i in range(len(char_alpha)):
            shift = i
            shifted_text = ''
            for n in range(len(text)):
                new_char = char_alpha[(char_alpha.index(text[n]) + i) % len(char_alpha)]
                shifted_text += new_char
            shifted_texts.append(shifted_text)
    return shifted_texts


# Run through all shifts for any ascii text using all ascii characters - or a provided alphabet - all together
def brute_shift_all_or_defined(text, alphabet):
    shifted_texts = []
    for i in range(len(alphabet)):
        shift = i
        shifted_text = ''
        for n in range(len(text)):
            new_char = alphabet[(alphabet.index(text[n]) + i) % len(alphabet)]
            shifted_text += new_char
        shifted_texts.append(shifted_text)
    return shifted_texts


# My naive way to exit the program neatly
def exit_tool():
    print("Thank you, come again!")


# A simple menu to choose what to do and provide the text or alphabet if applicable
def menu():
    print("Brutus - Cipher Brute-Forcing Tool V1.0")
    print("")
    valid_inputs = '123Qq'
    loop_cond = True
    while loop_cond == True:
        try:
            print("Would you like to use an alphanumeric alphabet, all ascii, or define your own?")
            selection = input("Correspondingly enter 1, 2, 3, or Q to exit: ")
            if selection not in valid_inputs:
                raise ValueError
            if selection == "1":
                user_text = input("Please enter the string you want to decode or encode: ")
                print(brute_shift_alphanumerics(user_text))
            elif selection == "2":
                user_text = input("Please enter the string you want to decode or encode: ")
                print(brute_shift_all_or_defined(user_text, all_chars))
            elif selection == "3":
                user_text = input("Please enter the string you want to decode or encode: ")
                user_defined_alphabet = input("Please enter your alphabet: ")
                print(brute_shift_all_or_defined(user_text, user_defined_alphabet))
            if selection == 'Q' or selection == 'q':
                loop_cond = False
                exit_tool()
        except ValueError:
            print('Enter a valid input!!')
    

# Run the stuff
def main():
    menu()

# Run the run the stuff
if __name__ == '__main__':
    main()









            

