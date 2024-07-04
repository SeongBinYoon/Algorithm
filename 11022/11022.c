// 11022 A + B - 8

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    int T;
    int a,b;
    scanf("%d", &T);
    for(int i = 0; i < T; i++){
        scanf("%d %d", &a, &b);
        printf("%s%d%s%d%s%d%s%d\n", "Case #", i + 1, ": ", a, " + ", b, " = ", a + b);
    }
    return 0;
}
