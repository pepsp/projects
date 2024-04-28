import random


def main():
    level = get_level("Level: ")
    randomNumber = random.randint(1, level)
    while True:
        try:
            respuesta = int(input("Guess: "))
            if respuesta == randomNumber:
                print("Just right!")
                break
            elif respuesta > randomNumber:
                print("Too large!")
                pass
            elif respuesta < 1:
                pass
            else:
                print("Too small!")
                pass
        except ValueError:
            pass


def get_level(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                raise ValueError
        except ValueError:
            pass


if __name__ == "__main__":
    main()
