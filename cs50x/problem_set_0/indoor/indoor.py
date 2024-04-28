def main():
    question = input("Let's use your indoor voice! ")
    print(indoor(question))


def indoor(text):
    return text.casefold()


main()
