import validators

def main():
    if email:= validators.email(input("What's your E-mail? ")):
        print("Valid")
    else:
        print("Invalid")


main()
