
def main():
    credit = get_credit()
    checksum = lunh(credit)
    is_valid(checksum, credit)


def get_credit():
    return (input("Credit card number: ").strip())



def lunh(card):
    total_sum = 0
    for i in range(len(card)-2, -1, -2):
        digit = int(card[i]) * 2
        if digit > 9:
            digit = (digit % 10) + (digit // 10)
        total_sum += digit

    for i in range(len(card) - 1, -1, -2):
        total_sum += int(card[i]) % 10
    return int(total_sum)


def is_valid(card, credit):
    if card % 10 == 0:
        if len(credit) == 15 and (credit[:2] == "34" or credit[:2] == '37'):
            print("AMEX")
        elif len(credit) == 16 and (int(credit[:2]) > 50 and int(credit[:2]) < 56):
            print("MASTERCARD")
        elif (len(credit) == 13 or len(credit) == 16) and credit[0] == "4":
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")


main()
