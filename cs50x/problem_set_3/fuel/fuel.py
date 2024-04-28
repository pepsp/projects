def main():
    percent = get_perc()
    if percent >= 0.9:
        print("F")
    elif percent <= 0.1:
        print("E")
    else:
        print(round(percent * 100), "%", sep="")


def get_perc():
    while True:
        try:
            frac = input("Fraction: ").split("/")
            x = int(frac[0])
            y = int(frac[1])
            if x > y:
                raise ValueError
            return x / y

        except (ValueError, ZeroDivisionError):
            pass


main()
