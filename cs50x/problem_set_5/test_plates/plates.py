def main():
    plate = input("Plate :")
    if is_valid(plate) == True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif (
        s[:2].isalpha()
        and s[2:].isdigit()
        and " " not in s
        and s[2] != "0"
        and s.isalnum()
    ):
        return True
    elif (
        s[:3].isalpha()
        and s[3:].isdigit()
        and " " not in s
        and s[3] != "0"
        and s.isalnum()
    ):
        return True
    elif s.isalpha() and " " not in s:
        return True
    return False


if __name__ == "__main__":
    main()
