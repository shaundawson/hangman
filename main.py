import random

#Create a list of words
word_list = ["Asexual", "Biphobia", "Deadnaming", "Homosexual", "Intersex", "Pronoun", "Queer", "Transphobia"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = str(random.choice(word_list))

# Split string to each letter 
def split(word): 
    return [char for char in word] 
chosen_word = (split(chosen_word.lower())) 


#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase. 
guess = input("Guess a letter\n")

#Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Generate as many blanks as letters in a word.
word2 = []
for l in chosen_word:  
    if l  == guess:
        word2.append(guess)
    else:
        word2.append('_')
print(word2)

#If the guessed letter is in the word, replace the blank letter and check if all the blanks are filled. If all the blanks are filled the game is over and you win. 


#If the guessed letter is not in the word, you lose a life. If you've run out of lives, the game is over and you lose. 