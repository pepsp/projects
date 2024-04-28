#include <stdio.h>
#include <cs50.h>

int main (void)
{
    int number = get_int("How many number do you want in your array? ");
    int n[number];

    for (int i = 0; i < number; i++){

        if (i == 0) {
            n[i] = 1;
        }else{
            n[i] = (n[i-1]) * 2;
        }

    }

    for (int i = 0; i < number; i++){
        printf("%i\n", n[i]);
    }
}
