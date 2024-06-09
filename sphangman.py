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

#Step 1 

word_list = ["Scott", "Ramona", "Julie", "Wallace", "Stacey","Knives", "Kim"]
display = []
lives = 6
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_length = len(str(chosen_word))
print(chosen_word)
for x in range(word_length):
    display += '_'
print(display)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
end_of_game = False
while end_of_game == False:
    guess = input("Guess a letter: ").lower()
    for index in range(word_length):
        letter=chosen_word[index].lower()
        if letter == guess:
           display[index] = letter
    
    print(display)




    
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    if "_" not in display:
        end_of_game = True
        print(f'You won with {lives} lives remaining.')
    print(stages[lives])