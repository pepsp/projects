from datetime import date
import inflect
import re
import sys

def main():
    p = inflect.engine()
    dob = get_dob()
    today = get_today()
    difference = get_diff(today, dob).days
    minutes = days_minutes(difference)
    print(p.number_to_words(minutes, andword ="").capitalize(), "minutes")


def get_dob():
    user_dob = input("D.O.B. : ").strip()
    matches = re.search(r"^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])$", user_dob)
    if matches:
        year, month, day = map(int, matches.groups())
        return date(year, month, day)
    else:
        sys.exit(1)

def get_today():
    return date.today()

def get_diff(dob, today):
    return (dob - today)

def days_minutes(days):
    return int(days * 24 * 60)


if __name__ == "__main__":
    main()
