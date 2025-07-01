# Hangman — Python CLI Game

This is a simple command-line implementation of the classic **Hangman** game, written in Python. Try to guess the hidden word, one letter at a time, before you run out of lives!

## Features

- ASCII art hangman stages for visual feedback
- Randomly selected words from a customizable list
- Tracks and displays correct guesses and remaining lives
- Informs the user about repeated guesses and incorrect attempts
- Shows the correct word if the player loses

## How to Play

1. **Run the script**:
    ```bash
    python hangman.py
    ```
2. The game will display a series of underscores representing the hidden word.
3. Guess one letter at a time by typing it and pressing Enter.
4. If the letter is in the word, all instances are revealed.
5. If the letter is not in the word, you lose a life and the hangman drawing progresses.
6. The game ends when you either guess all the letters or run out of lives.

## Example Gameplay

```
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    

Word to guess: _____
****************************6/6 LIVES LEFT****************************
Guess a letter: a
Word to guess: a____
****************************6/6 LIVES LEFT****************************
Guess a letter: e
You guessed e, that's not in the word. You lose a life
Word to guess: a____
  +---+
  |   |
  O   |
      |
      |
      |
=========
...
***********************IT WAS apple YOU LOSE**********************
```

## Requirements

- Python 3.x

## Customization

- Add or change words in the `word_list` variable.
- Adjust the number of lives or hangman stages as desired.

## Getting Started

1. Save the code as `hangman.py`.
2. Open a terminal and navigate to the file's directory.
3. Run the game with:
    ```bash
    python hangman.py
    ```

## Author

- [Subham Nayak](https://github.com/Subham73-cmd)


Enjoy playing Hangman!
