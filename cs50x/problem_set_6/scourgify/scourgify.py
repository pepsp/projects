import csv
import sys


def main():
    try:
        read, write = command_check(sys.argv)
        data = get_files(read)
        write_files(write, data)

    except ValueError as ve:
        print(ve)
        sys.exit(1)
    except FileNotFoundError as fnfe:
        print(fnfe)
        sys.exit(1)
    except IndexError as ie:
        print(ie)
        sys.exit(1)


def command_check(argv):
    if len(argv) < 3:
        raise IndexError("Too few command-line arguments")
    elif len(argv) > 3:
        raise IndexError("Too many command-line arguments")
    elif len(argv) == 3 and argv[1].endswith(".csv") and argv[2].endswith(".csv"):
        return argv[1], argv[2]
    else:
        raise ValueError("Not a CSV file")


def get_files(x):
    try:
        with open(x) as file:
            reader = csv.DictReader(file)
            data = [dict(row) for row in reader]
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not read {x}")


def write_files(y, data):
    with open(y, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in data:
            last_name, first_name = row["name"].split(", ")
            writer.writerow(
                {"first": first_name, "last": last_name, "house": row["house"]}
            )


if __name__ == "__main__":
    main()
