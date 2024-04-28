#include <stdio.h>
#include <cs50.h>

int steps = 0;
int collatz(int n);
int main (void)

{
    int n = get_int("Number: ");
    printf("%i Steps\n",collatz(n));
}


int collatz(int n)
{
    if (n == 1){
        return 0;
    }

    if (n % 2 == 0){
        steps++;
        collatz(n /2);
    }else if (n % 2 != 0){
        steps++;
        collatz((3 * n) + 1);
    }

        return steps;
}


