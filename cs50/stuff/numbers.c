#include <cs50.h>
#include <stdio.h>
int add(int a, int b);

int main(void){
    int x = get_int("X: ");
    int y = get_int("Y: ");
    printf("%i\n", add(x, y));
}

int add(int a, int b){
    return a + b;
}
