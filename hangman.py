# Hard-code a word that needs to be guessed in the script

from itertools import count


guess_word = "hello"


# Print an explanation to the user
print("""Hello ! Welcome to the classical hangman game. 
Your task will be to guess the right word until you get it correctly. 
You only have few attempts
\nGuess the Word!""")


#Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

for letter in guess_word:
    print("_", end=" ")



#Create a counter for how many tries a user has
counter = 0
word = ""

while counter != 10:
    #Ask for user input
    #Allow only single-character alphabetic input
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    while True:
        user_input = str.lower(input("\nInsert a single-character alphabetic input:"))
        if user_input in alphabet:
            break
    #check if user_input is the same as a letter in a word
    for letter in guess_word:
        if user_input == letter:
            word = letter
        else:
            word = "_"

    # blindspot the rest
    for letter in guess_word():
        if letter == word:
            print(letter, end=" ")


    if word ==guess_word:
        break
    
    counter += 1




