def main():
    plate = input("Plate :")
    if is_valid(plate) == True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        if s[0].isnumeric() == False and s[1].isnumeric() == False:
            if (
                s[-1].isnumeric()
                and s[-2].isnumeric()
                and s[-2] != "0"
                or s[-1].isnumeric() == False
                and s[-2].isnumeric() == False
            ):
                if (
                    s.find(" ") < 0
                    and s.find(".") < 0
                    and s.find("'") < 0
                    and s.find("-") < 0
                    and s.find("?") < 0
                    and s.find("!") < 0
                    and s.find(",") < 0
                ):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


main()
