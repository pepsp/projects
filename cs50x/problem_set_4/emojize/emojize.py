import emoji


def main():
    convert = input("Input: ")
    print("Output: ", emoji.emojize(convert, language="alias"))


main()
