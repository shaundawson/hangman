from replit import clear
import random

from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = str(random.choice(word_list))

#Testing code
# print(f"Psst, ths solution is {chosen_word}")

#Create blanks 
display = []
# Store length of word in a variable
word_length = len(chosen_word)
#Store number of lives left in a variable 
lives = 6
end_of_game = False

#For each letter in the chosen_word, add a "_" to display
for _ in range(word_length):
    display += "_"
print(display)
    
# While there are blanks in display
while not end_of_game:
    #Ask the user to guess a letter and assign their answer to a variable called guess. 
    guess = input("Guess a letter:").lower()

    clear()
    
    if guess in display:
        print(f"You've already guessed '{guess}'. Please choose another letter.")
    
    #Loop through each position in the chosen_word 
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        #If the letter in that position  matches 'guess' 
        if letter  == guess:
            #Reveal that letter in the display at postion
            display[position] = letter

    #Check if user is wrong
    if guess not in chosen_word:
        print(f"You guessed {guess}. This letter is not in the word. You lose a life.")
        # if guess is not a letter in the chosen_word, reduce lives by 1
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Show the guessed letter in the correct position and every other letter replace with "_". Turn it into a string
    print(f"{' '.join(display)}")

    #Check to see if it's the end of game
    if "_" not in display:
        end_of_game = True
        print("You win!")

    #Print the ascii art from stages that corresponds with the current number of lives the user has remaining
    print(stages[lives])
