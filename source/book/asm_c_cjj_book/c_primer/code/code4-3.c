//praise2.c  使用不同类型的字符串
//如果编译器识别不了%zd  尝试换成%u或者%lu
#include <stdio.h>
#include <string.h>
#define PRAISE 'you str an exterraodinaty bering'
int main(void){
    char name[40];
    printf("wath you name");
    scanf("%s",name);
    print("hello %s, .%s \n",name,PRAISE);
    print("your %zd letters ",strlen(name));
    print("%zd",sizeof PRAISE);
    return 0;
}