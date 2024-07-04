// 25304 영수증

#include <stdio.h>

int main(){
    int total_price, num_prod = 0;
    int price, amt, pred_price = 0;
    scanf("%d\n%d\n", &total_price, &num_prod);
    
    // 반복적으로 받기
    for (int i = 0; i < num_prod; i++){
        scanf("%d %d", &price, &amt);
        pred_price += price * amt;
    }
    // 조건문으로 yes, no 구분
    if (total_price == pred_price)
        printf("Yes");
    else
        printf("No");
    
}