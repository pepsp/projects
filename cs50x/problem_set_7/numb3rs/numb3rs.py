import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    matches = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    if matches:
        a, b, c, d = matches.groups()
        if int(a) <= 255 and int(b) <= 255 and int(c) <= 255 and int(d) <= 255:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
