import csv
from tabulate import tabulate
import sys

def main():
    try:
        result = get_tabulate(command_check(sys.argv))
        print(tabulate(result, headers ="keys", tablefmt = "grid" ))

    except ValueError as ve:
        print(ve)
        sys.exit(1)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    except IndexError as ie:
        print(ie)
        sys.exit(1)


def command_check(argv):
    if len(argv) == 1:
        raise IndexError("Too few command-line arguments")
    elif len(argv) > 2:
        raise IndexError("Too many command-line arguments")
    elif len(argv) == 2 and argv[1].endswith(".csv"):
        return argv[1]
    else:
        raise ValueError("Not a CSV file")

def get_tabulate(file_name):
    try:
        with open(file_name) as file:
            reader = csv.DictReader(file)
            data = [dict(row) for row in reader]
            return data


    except FileNotFoundError:
        raise FileNotFoundError


if __name__ == "__main__":
    main()


