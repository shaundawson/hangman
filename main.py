import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Create a list of words
word_list = ["Asexual", "Biphobia", "Deadnaming", "Homosexual", "Intersex", "Pronoun", "Queer", "Transphobia", "Ally", "Cisgender", "Genderqueer", "Pansexual", "Polyamnory", "Transmasculine", "Heterosexism", "Passing", "Oppression", "Prejudice", "Discrimination", "Cisnormativity", "Transfeminine", "Androgynous", "Androsexual", "Demiromantic", "Fluid", "Gynosexual", "Masculinity", "Omnisexual", "Queerplatonic", "Sapiosexual", "Skoliosexual", "Sexuality", "Stealth", "Stereotype"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = str(random.choice(word_list))

#Testing code
print(f"Psst, ths solution is {chosen_word}")

# Split string to each letter 
def split(word): 
    return [char for char in word] 
chosen_word = (split(chosen_word.lower()))

#Create an empty list called display. 
display = []
# Store length of word in a variable
word_length = len(chosen_word)
#For each letter in the chosen_word, add a "_" to display
for _ in range(word_length):
    display += "_"
print(display)

#Store number of lives left in a variable 
lives = 6
end_of_game = False

    
# while there are blanks in display
while not end_of_game:
    #Ask the user to guess a letter and assign their answer to a variable called guess. 
    guess = input("Guess a letter:").lower()
    #Loop through each position in the chosen_word 
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        #If the letter in that position  matches 'guess' 
        if letter  == guess:
            #Reveal that letter in the display at postion
            display[position] = letter
            
    if guess not in chosen_word:
        # if guess is not a letter in the chosen_word, reduce lives by 1
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Show the guessed letter in the correct position and every other letter replace with "_"
    print(f"{' '.join(display)}")

    #Check to see if it's the end of game
    if "_" not in display:
        end_of_game = True
        print("You win!")

    #Print the ascii art from stages that corresponds with the current number of lives the user has remaining
    print(stages[lives])
