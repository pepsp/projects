#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

char key[26];
int main(int argc, string argv[])
{
    // Validating command-line length
    if (argc != 2)
    {
        printf("Usage: %s key\n", argv[0]);
        return 1;
    }
    // Validating key length
    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain exactly 26 alphabetic characters\n");
        return 1;
    }

    // Check for non-alpha
    for (int i = 0, len = strlen(argv[1]); i < len; i++)
    {
        if (ispunct(argv[1][i]))
        {
            printf("Symbols are not valid as key\n");
            return 1;
        }
    }

    // Check for repetition - case insensitive
    for (int i = 0, len = strlen(argv[1]); i < len; i++)
    {
        for (int j = i + 1; j < len; j++)
        {
            if (tolower(argv[1][i]) == tolower(argv[1][j]))
            {
                printf("Repeted key characters are not allowed\n");
                return 1;
            }
        }
    }

    // Store command-line key to key array
    if (strlen(argv[1]) == 26)
    {
        for (int i = 0, len = strlen(argv[1]); i < len; i++)
        {
            key[i] = argv[1][i];
        }
    }
    // Get word to convert using key
    string keyword = get_string("plaintext: ");

    printf("ciphertext: ");
    for (int i = 0, len = strlen(keyword); i < len; i++)
    {
        if (isupper(keyword[i]))
        {
            printf("%c", toupper(key[keyword[i] - 'A']));
        }
        else if (islower(keyword[i]))
        {
            printf("%c", tolower(key[keyword[i] - 'a']));
        }
        else
        {
            printf("%c", keyword[i]);
        }
    }
    printf("\n");
    return 0;
}
