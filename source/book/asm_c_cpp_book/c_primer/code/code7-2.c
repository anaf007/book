//ctype.c //替换输入的字符

#include <stdio.h>
int main(void){
    char ch;
    while((ch=getchar())!= '\n'){
        if(isalpha()){          //如果是一个空字符
            putchar(ch+1);       //显示该字符的下一个字符
        }else{
            putchar(ch);
        }
    }
    putchar(ch);        //显示换行符
    return 0;
}