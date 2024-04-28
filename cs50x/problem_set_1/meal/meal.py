def main():
    whatTime = input("What time is it? ")
    if convert(whatTime) >= 7 and convert(whatTime) <= 8:
        print("breakfast time")
    elif convert(whatTime) >= 12 and convert(whatTime) <= 13:
        print("lunch time")
    elif convert(whatTime) >= 18 and convert(whatTime) <= 19:
        print("dinner time")


def convert(time):
    return float(time.split(":")[0]) + float(time.split(":")[-1]) / float(60)


if __name__ == "__main__":
    main()
