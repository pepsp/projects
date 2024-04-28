def main():
    palabra = input("Input: ")
    no_vocales = ""
    for i in palabra:
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
            no_vocales += i
        else:
            no_vocales += ""
    print(f"Output: {no_vocales}")


main()
