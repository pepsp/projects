from hangman_data import get_hang
from hangman_data import difficulty
import random
import sys
import cowsay
from pyfiglet import Figlet


def main():
    f = Figlet(font='doom')
    done = False
    diff = select_difficulty()
    secret_word = get_word(diff)
    lives = 0
    print(f.renderText("\nLet's start the game!!\n"))
    guessed_letters = []

    while not done:
        get_hang(lives)

        for letter in secret_word:
            if letter.casefold() in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")

        print(previous_guess(guessed_letters))
        current_guess = input("\nEnter yor guess: \n".casefold())

        if len(current_guess) != 1 or not current_guess.isalpha():
            print("\nPlease, only input one letter per turn\n")
            continue
        if current_guess.casefold() in guessed_letters:
            print("\nYou already tried that letter, please try another!\n")
            continue

        guessed_letters.append(current_guess.casefold())

        if current_guess.casefold() not in secret_word.casefold():
            lives += 1
            if lives < 6:
                print("\nIncorrect guess, please try again\n")
        if lives == 6:
            get_hang(6)
            print(f"\nSorry, you lost the game!, the word was {secret_word}\n")
            done = True
        if set(secret_word).issubset(guessed_letters):
            print(f.renderText(f"\nCongratulations!, you guessed the word {secret_word} \n"))
            done = True

        if done == True:
            while True:
                state = input("Game over, would you like to try again? Y/N \n").casefold()
                if state == "y":
                    main()
                elif state == "n":
                    f = Figlet(font="roman")
                    print(f.renderText("\nThank you for playing!\n"))
                    credits = ("\n\nCreated by Jose C. Obregon, February 5th, 2024\n\n")
                    cowsay.cow(credits)
                    sys.exit()
                else:
                    print("Please answer yes (y) or no(n)")
                    pass


def get_word(diff):
    match diff:
        case 1:
            return random.choice(difficulty["easy"])
        case 2:
            return random.choice(difficulty["hard"])
        case 3:
            while True:
                custom_word = input("Input: \n").strip()
                if len(custom_word) >= 4 and len(custom_word) <= 10 and custom_word.isalpha():
                    return custom_word.casefold()
                else:
                    print("\nATTENTION:  \nYou must use a 4-letter word minimum, 10-letter word maximum!\n")


def select_difficulty(input_function=input):
    while True:
        diff = (
            input_function(
                "\nSelect difficulty: \n\n1. EASY -- (4 letters)\n\n2. HARD -- (10 letters)\n\n3. CUSTOM WORD (2-PLAYER MODE)\n\n0. EXIT\n"
            )
            .casefold()
            .strip()
        )
        if diff in ["easy", "1", "e"]:
            return 1
        elif diff in ["hard", "2", "h"]:
            return 2
        elif diff in ["custom", "3", "c"]:
            return 3
        elif diff in ["exit", "0"]:
            sys.exit()
        else:
            print("\nNot a valid option, please try again\n")


def previous_guess(guess):
    if guess == []:
        return "\nGood luck!\n"
    else:
        guessed_letters = ' '.join(guess)
        return f"\n↓↓ Previously guessed letters ↓↓\n {guessed_letters} "


if __name__ == "__main__":
    main()
