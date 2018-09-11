// file:talkback.c
#include <stdio.h>
#include <string.h>
#define DENSITY 62.4

int main(){
    float weight,volume;
    int size,letters;
    char name[40];

    printf("you name\n");
    scanf('%s',name);
    print('%s nameis ',name);
    scanf('%f',&weight);
    size = sizeof name;

    letters = strlen(name);

    volume = weight/DENSITY;

    printf("well %s ,you volume is %2.2f cuble \n",name,volume );

    return 0;
}
