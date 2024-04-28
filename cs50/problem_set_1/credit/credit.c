#include <cs50.h>
#include <stdio.h>

int main(void)

{

    long long card_number;
    int length = 0; // keeps count of the lenght of the card
    int sum = 0;    // keeps track of checksum

    do
    {

        card_number = get_long_long("Card Number: ");
    }

    while (card_number < 0);

    // every other number. starting from second-to-last

    for (long long i = card_number / 10; i > 0; i /= 100)
    {

        int digit = (i % 10) * 2;
        sum += digit / 10 + digit % 10;
        length++;
    }
    //

    // rest of the numbers not multiplied by 2
    for (long long i = card_number; i > 0; i /= 100)
    {
        int digit = i % 10;
        sum += digit;
        length++;
    }
    //

    // checksum
    if (sum % 10 == 0)
    {

        if (length == 15 && (card_number / 10000000000000 == 34 || card_number / 10000000000000 == 37))
        {
            printf("AMEX\n");
        }
        else if (length == 16 && (card_number / 100000000000000 > 50 && card_number / 100000000000000 < 56))
        {
            printf("MASTERCARD\n");
        }
        else if ((length == 13 || length == 16) && (card_number / 1000000000000 == 4 || card_number / 1000000000000000 == 4))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}
/// checksum
