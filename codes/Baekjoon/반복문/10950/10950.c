// 10950 A + B - 3

#include <stdio.h>

int main() {
    // insert code here...
    int N,a,b;
    scanf("%d\n", &N);
    for(int i = 0; i < N; i++){
        scanf("%d %d\n", &a, &b);
        printf("%d\n", a + b);
    }
    

    return 0;
}
