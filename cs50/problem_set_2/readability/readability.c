#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
float coleman_index(int letter, int word, int sentence);
void get_grade(float n);
int main(void)
{
    string text = get_string("Text: ");

    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);
    float index = coleman_index(letters, words, sentences);
    get_grade(index);
}

int count_letters(string text)
{
    int letters = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {

        if (isalpha(text[i]))
        {
            letters++;
        }
    }

    return letters;
}

int count_words(string text)
{
    int words = 0;

    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isalpha(text[i]) && isspace(text[i + 1]))
        {
            words++;
        }
        else if (ispunct(text[i]) && isspace(text[i + 1]))
        {
            words++;
        }
        else if (i == len - 1 && (isalpha(text[i]) || (ispunct(text[i]))))
        {
            words++;
        }
    }
    return words;
}

int count_sentences(string text)
{
    int sentences = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {

        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
        else if (i == len - 1 && isalpha(text[i]))
        {
            sentences++;
        }
    }
    return sentences;
}

float coleman_index(int letter, int word, int sentence)
{

    float l = (float) letter / word * 100;
    float s = (float) sentence / word * 100;

    float index = 0.0588 * l - 0.296 * s - 15.8;
    return round(index);
}

void get_grade(float n)
{
    if (n < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (n >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int) n);
    }
}
