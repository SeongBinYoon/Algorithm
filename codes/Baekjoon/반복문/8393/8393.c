// 8393 합

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    int n;
    int arr = 0;
    int sum = 0;
    scanf("%d", &n);
    for(int i = 1; i <= n; i++){
        arr = i;
        sum = sum + arr;
    }
    printf("%d\n",sum);
    return 0;
}
