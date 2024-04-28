def main():
    total_amount = int(50)
    while total_amount > 0:
        coin = int(input(f"Amount Due: {total_amount}\n"))
        if (
            coin > 0
            and coin == int(25)
            or coin == int(50)
            or coin == int(10)
            or coin == int(5)
        ):
            total_amount -= coin
    if total_amount <= 0:
        print(f"Change Owed: {total_amount*-1}")


main()
