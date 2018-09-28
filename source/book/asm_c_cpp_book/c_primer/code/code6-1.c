#include <stdio.h>

int main(void){
    long num;
    long sum = 0L;
    int status;

    status = scanf("%ld",&num);
    while(status ==1){
        status = scanf("%ld",&num);
    }

    return 0;

}