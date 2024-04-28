def main():
    mass = int(input("M: "))
    print("E: ", mass * light(300000000))


def light(n):
    return pow(n, 2)


main()
