//two_func.c 一个文件中包含两个函数

#include <stdio.h>
void butler(void);  //snsi/iso c函数原型

int main(void){
    printf("main_start\n");
    butler()
    printf("main_end\n");

    return 0;
}

void butler(void){
    printf("butler\n");
}