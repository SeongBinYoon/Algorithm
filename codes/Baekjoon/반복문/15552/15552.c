// 15552 빠른 A + B

#include <stdio.h>

int main() {
    // insert code here...
    int T;
    int a,b;
    scanf("%d", &T);
    for(int i = 0; i < T; i++){
        scanf("%d %d", &a, &b);
        printf("%d", a+b);
    }
    return 0;
}
