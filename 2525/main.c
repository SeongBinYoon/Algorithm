#include <stdio.h>

int main(){
    // h = hour, m = minute, a = add time
    int h, m, a = 0;
    scanf("%d %d\n %d", &h, &m, &a);

    int add_h = (m + a) / 60;
    h = h + add_h;
    m = (m + a) % 60;
    // h는 0~23까지만
    if (h > 23)
        h = h % 24;
    printf("%d %d\n", h, m);
}