import random

#Create a list of words
word_list = ["Asexual", "Biphobia", "Deadnaming", "Homosexual", "Intersex", "Pronoun", "Queer", "Transphobia"]

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
    
#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase. 
guess = input("Guess a letter:").lower()


#Loop through each position in the chosen_word 
for position in range(word_length):
    letter = chosen_word[position]
     #If the letter in that position  matches 'guess' 
    if letter  == guess:
        #Reveal that letter in the display at postion
        display[position] = letter

print(display)
