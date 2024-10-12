// 1110 더하기 사이클

#include <stdio.h>

int main() {
    int n;
    int cnt = 0;
    int result; //결과물이 처음입력값과 같은지를 확인해줄 수 있는 검문소 정의
    int c;
    int tmp;
    scanf("%d", &n);
    result = n; //검문소
    while(1){
        c = ((n / 10) + (n % 10));
        tmp = ((n % 10) * 10 + (c % 10));
        n = tmp; //while문안에서 tmp값이 새로운 n값이 되도록(순환) 선언
        cnt++;
        if(tmp == result){
            break;
        }
    }
    printf("%d\n",cnt);
    
}

