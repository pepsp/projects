import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        tries = 0
        x = generate_integer(level)
        y = generate_integer(level)
        problema = x + y
        while tries < 3:
            try:
                respuesta = int(input(f"{x} + {y} = "))
                if respuesta == problema:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1
        if tries == 3:
            print(f"{x} + {y} =", problema)

    print("Score:", score)


def get_level():
    while True:
        try:
            value = int(input("Level: "))
            if value > 0 and value <= 3:
                return value
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        return x
    elif level == 2:
        x = random.randint(10, 99)
        return x
    else:
        x = random.randint(100, 999)
        return x


if __name__ == "__main__":
    main()
