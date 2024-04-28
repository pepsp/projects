def main():
    camel = input("camelCase: ")
    snake = ""
    for letra in camel:
        if letra.isupper() != True:
            snake += letra
        else:
            snake += f"_{letra}"
    print(snake.casefold())


main()
