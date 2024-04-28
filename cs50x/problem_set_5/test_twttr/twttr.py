def main():
    x = shorten(input("Input: "))
    print(x)


def shorten(word):
    word_new = ""
    for i in word:
        if (
            i != "a"
            and i != "e"
            and i != "i"
            and i != "o"
            and i != "u"
            and i != "A"
            and i != "E"
            and i != "I"
            and i != "O"
            and i != "U"
        ):
            word_new += i
        else:
            pass
    return word_new


if __name__ == "__main__":
    main()
