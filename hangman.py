# Hard-code a word that needs to be guessed in the script


from calendar import c


guess_word = "hello"


# Print an explanation to the user
print("""Hello ! Welcome to the classical hangman game. 
Your task will be to guess the right word until you get it correctly. 
You only have few attempts
\nGuess the Word!""")


#Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"





#Create a counter for how many tries a user has


word_list = ["_","_","_","_","_"]
counter = 0

while counter != 10:
    for letter in word_list:
        print(letter, end =" ")
    
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    while True:
        user_input = str.lower(input("\nInsert a single-character alphabetic input:"))
        if user_input in alphabet:
            break
        else:
            print("wrong input, try again")
    if user_input in guess_word:
        for index,letter in enumerate(guess_word):
            if user_input == letter:
                word_list[index] = user_input
                print("You got the letter right")
    else:
        counter += 1
        print (f"You got it wrong, you have {10 - counter} options left.")   


    conactenated_word = word_list[0] + word_list[1] + word_list[2] + word_list[3] + word_list[4]

    if conactenated_word == guess_word:
        print("You have won! Congratulations!")
        break

if counter == 10:
    print("You have lost the game!")

    
