//filename: pound.c

#include <stdio.h>
void pound(int n);

int main(void){
    int time = 5;
    char ch = '!';  //ASCII码为33；
    float f = 6.0f;

    pound(time);
    pound(ch);      //pound((int)ch)
    pound(f);       //pound((int)f)

    return 0;
}

void pound(int n){
    while(n-- > 0)
        printf("#");
    printf("\n");
}