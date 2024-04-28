#include <cs50.h>
#include <stdio.h>

void print_str(int lenght, string x);
void pyramid(int height);

int main(void)
{
    int height;
    do
    {
        height = get_int("Pyramid height: ");
        pyramid(height);
    }
    while (height < 1);
}

void print_str(int lenght, string x)
{
    for (int i = 0; i < lenght; i++)
    {
        printf("%s", x);
    }
}

void pyramid(int height)
{
    int x = height;

    for (int j = 1; j <= height; j++)
    {
        x--;
        print_str(x, " ");
        print_str(j, "#");
        print_str(2, " ");
        print_str(j, "#");
        printf("\n");
    }
}
