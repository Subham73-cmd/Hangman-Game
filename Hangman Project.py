import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
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

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
word_list=["Car","Rocket","Cargo","Sun","Moon"] #List of words. You can add more
lives=6 #No of lives
print(logo)
chosen_word = random.choice(word_list).lower()
placeholder = ""
word_length = len(chosen_word) #Length of the chosen word
for position in range(word_length):
    placeholder += "_" #Gives '_' in place of blanks=no of letters in the word
print("Word to guess: " + placeholder)
game_over = False   #Initiating game over to be false
correct_letters = [] #Empty list for correct letters
while not game_over:   #It run the program in a loop till the game over remains false
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    #Prints no of lives remains out of the total
    guess = input("Guess a letter: ").lower()
    #Takes input from user both in uppercase and lowercase
    if guess in correct_letters:
        print(f"You already guess the letter {guess}")
        #Prints this statement if the gues is already in the correct_letters
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)  #Appends the guess into correct letters and stores them
        elif letter in correct_letters:
            display += letter #If letter is already in the correct list it displays it
        else:
            display += "_"  #If guess is incorrect it displays '_' inplace of blank
    print("Word to guess: " + display)
    if guess not in chosen_word:
        lives -= 1   #If guess is not in chosen word, it deducts lives by 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        if lives == 0:
            game_over = True  #If lives is 0 then game is over
            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************IT WAS {chosen_word} YOU LOSE**********************")
            # If you lose it gives the coreect word
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
        #If there are no blanks or '_' in display then you win
    print(stages[lives])
