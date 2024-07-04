// 10952 A + B - 5

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    int a,b;

    while(1){
        scanf("%d %d", &a, &b);
        if(a == 0 && b == 0){
            break;
        }
        else
            printf("%d\n", a + b);
       
    }
        
    return 0;
}
