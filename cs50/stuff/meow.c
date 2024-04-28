#include <stdio.h>
#include <cs50.h>

void meow(void);
int main(void){
    meow();
    }

void meow(void){
    int counter = get_int("How many times will you meow? ");
    for (int i = 0; i < counter; i++){
        printf("meow\n");
}
}
