// 2753 윤년

#include <stdio.h>

int main() {
    // insert code here...
    int a;
    scanf("%d", &a);
    if((a % 4 == 0 && a % 100 != 0) || (a % 400 == 0)){
        printf("1\n");
    }
    else
        printf("0\n");
    
    return 0;
}
