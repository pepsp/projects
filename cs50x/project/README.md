# HANGED MAN GAME
#### Video Demo: <https://youtu.be/_JXw7A4_B0w>
#### Description:
### Play alone or with your friends with this hang-man game!
### Easy and hard difficulty, with 20 possible answers each!
### Use a custom word, 4 letters minimum, 10 letters maximum
### hangman_data

This file contains a dict (**hangman_lives**) used for displaying remaining lives graphically, representing each body part of the hanged man based on the remaining lives. It also contains a directory (**difficulty**) that stores words categorized by their difficulty level. Easy words are 4 letters long, and hard words are 10 letters long. The function **get_hang(n)** prints the remaining lives using the **hangman_lives** directory.

### Main file

In the main file, I used several libraries to display text in a visually appealing manner:

- **pyfiglet**: Displays large letters generated from ordinary text. I used it to reward the player with a congratulatory message upon guessing a word correctly.
- **cowsay**: Renders ASCII art of a cute cow saying any input text. I utilized it to display my name as credits when exiting the program.
- **Random library**: Aids in choosing a random word from the **difficulty** dictionary, depending on the player's selected difficulty.
- **sys**: Facilitates program termination when prompted.

## Functions

### get_word(diff)

This function returns a word depending on the user's input from the **select_difficulty()** function. It accesses the **difficulty** library and retrieves a word based on the chosen case:
- If the case is 3, the function asks for player input and returns that word, stripped and casefolded.
- If the word contains numbers or symbols, or if it's more than 10 letters or less than 4, it will display an error message and re-ask for input.

### select_difficulty()

This function returns 1, 2, or 3 depending on the difficulty chosen by the user, or returns 0 if the user wants to exit the program. The input is case insensitive:
- Easy = easy, e, or 1
- Hard = hard, h, or 2
- Custom = custom, c, or 3
- Exit = exit or 0
If another letter is input, it will display an error message and reprompt.

### previous_guess(guess)

This function appends all of the already guessed letters to the **guessed_letters** array. If the array is empty, it prints "Good luck!".

## main()
### The rest of my code is stored in my **main** function

## Initialization and Setup
1. **Figlet Initialization**: Initializes a Figlet object for ASCII art.
2. **Game Setup**:
    - `done`: Boolean variable to control the game loop.
    - `diff`: Retrieves the difficulty level selected by the player.
    - `secret_word`: Obtains a secret word based on the chosen difficulty level.
    - `lives`: Tracks the number of incorrect guesses made by the player.
    - `guessed_letters`: Stores letters already guessed by the player.

## Gameplay Loop
### **Display Hangman State**: current state of the hangman, based on the number of incorrect guesses (`lives`).
### **Display Guessed Letters and Underscores**: Prints the secret word with guessed letters revealed and underscores for unguessed letters.
### **Prompt for Player Input**: Requests the player to input a one-letter guess.
### **Input Validation**:
    - Checks if the input is a single alphabetic character.
    - Verifies if the letter has already been guessed.
### **Update Guessed Letters**: Adds the guessed letter to the list.
### **Check Guess Outcome**:
    - If the guessed letter is not in the secret word, increments `lives`.
    - If the player runs out of lives, ends the game and reveals the secret word.
    - If all letters in the secret word have been guessed, ends the game with a victory message.
### **Game Over Handling**:
    - Prompts the player if they want to play again.
    - Handles player input validation for replay option.
    - Restarts the game or exits based on player choice, displays credits if exit.

## Credits
- **Author**: Jose C. Obregon
- **Creation Date**: February 5th, 2024





