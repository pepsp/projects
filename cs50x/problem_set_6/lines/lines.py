import sys


def main():
    try:
        result = get_file(command_check(sys.argv))
        print(result)

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
    elif argv[1].endswith(".py"):
        return argv[1]
    else:
        raise ValueError("Not a python file")


def get_file(file_name):
    try:
        with open(file_name) as file:
            num_lines = 0
            for line in file:
                strip_line = line.strip()
                if strip_line and not strip_line.startswith("#"):
                    num_lines += 1
        return num_lines
    except FileNotFoundError:
        raise FileNotFoundError


if __name__ == "__main__":
    main()
