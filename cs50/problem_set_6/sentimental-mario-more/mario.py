def main():
    height = get_height()
    print_pyramid(height)


def get_height():
    while True:
        try:
            height = int(input("Height of pyramid: "))
            if height > 0 and height <= 8:
                return height
        except ValueError:
            pass


def print_pyramid(height):
    for i in range(1, height + 1):
        print(f"{' ' * (height - i)}{'#' * i}  {'#' * i}")


main()
