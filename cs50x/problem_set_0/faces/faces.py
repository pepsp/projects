def main():
    change = input("Let's modernize your emoticons! ")
    print(
        change.replace(
            ":)",
            "🙂",
        ).replace(":(", "🙁")
    )


main()
