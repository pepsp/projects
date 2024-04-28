// Implements a dictionary's functionality

#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

unsigned int size_count = 0;

// TODO: Choose number of buckets in hash table
const unsigned int N = 37;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int index = hash(word);
    node *n = table[index];
    while (n != NULL)
    {
        if (strcasecmp(n->word, word) == 0)
        {
            return true;
        }
        else
        {
            n = n->next;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int hash_v = 0;
    unsigned int prime = N;
    while (*word != '\0')
    {
        hash_v = hash_v * prime + tolower(*word);
        word++;
    }
    return hash_v % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *f = fopen(dictionary, "r");
    if (f == NULL)
    {
        printf("Could not open dictionary \n");
        return false;
    }
    char word[LENGTH + 1];

    while (fscanf(f, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("Could not allocate memory\n");
            return false;
        }
        int index = hash(word);
        strcpy(n->word, word);
        n->next = table[index];
        table[index] = n;
        size_count++;
    }
    fclose(f);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return size_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *n = table[i];
        while (n != NULL)
        {
            node *temp = n;
            n = n->next;
            free(temp);
        }
    }
    return true;
}
