def main():
    print(value(input("Greeting: ")))

def value(greeting):
    if greeting.casefold().startswith("hello"):
        return 0
    elif greeting.casefold().startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
