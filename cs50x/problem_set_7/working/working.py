import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        print("ValueError")
        sys.exit(1)


def convert(s):
    try:
        time_format = re.search(
            r"([0-9][0-2]?)(:([0-5]\d))? ([A|P]M) to ([0-9][0-2]?)(:([0-5]\d))? ([A|P]M)",
            s,
        )

        if time_format:
            partes = time_format.groups()
            if int(partes[0]) > 12 or int(partes[4]) > 12:
                raise ValueError
            primer_hora = new_format(partes[0], partes[2], partes[3])
            segunda_hora = new_format(partes[4], partes[6], partes[7])
            return primer_hora + " to " + segunda_hora
        else:
            raise ValueError

    except ValueError:
        raise ValueError


def new_format(hora, minuto, am_pm):
    if am_pm == "PM":
        if int(hora) == 12:
            new_hora = 12
        else:
            new_hora = int(hora) + 12
    else:
        if int(hora) == 12:
            new_hora = 0
        else:
            new_hora = int(hora)
    if minuto == None:
        new_minuto = "00"
        new_format = f"{new_hora:02}:{new_minuto}"
    else:
        new_format = f"{new_hora:02}:{minuto}"
    return new_format


if __name__ == "__main__":
    main()
