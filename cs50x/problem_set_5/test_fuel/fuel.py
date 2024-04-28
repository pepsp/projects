def main():
    porcentaje = convert(input("Fuel: "))
    print(gauge(porcentaje))

def convert(fraction):
    try:
        if "/" not in fraction:
            raise ValueError
        frac = fraction.split("/")
        x = (frac[0])
        y = (frac[1])

        if int(y) == 0:
            raise ZeroDivisionError
        elif x > y or not x.isnumeric() or not y.isnumeric():
            raise ValueError
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError
    rounded = round((int(x) / int(y)) * 100)
    return rounded


def gauge(percentage):
    if not str(percentage).isdigit():
        return percentage
    elif percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"




if __name__ == "__main__":
    main()
