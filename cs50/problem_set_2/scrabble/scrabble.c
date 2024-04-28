#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int SCRABBLE[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int get_score(string word);
void decide_winner(int player1, int player2);
int main(void)
{
    string word1 = get_string("Player 1's word: ");
    string word2 = get_string("Player 2's word: ");
    decide_winner(get_score(word1), get_score(word2));
}

int get_score(string word)
{
    int score = 0;
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        if (islower(word[i]))
        {
            score += SCRABBLE[word[i] - 'a'];
        }
        else if (isupper(word[i]))
        {
            score += SCRABBLE[word[i] - 'A'];
        }
    }
    return score;
}

void decide_winner(int player1, int player2)
{
    if (player1 > player2)
    {
        printf("Player 1 wins!\n");
    }
    else if (player2 > player1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}
