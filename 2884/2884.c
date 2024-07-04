// 2884 알람 시계

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    int h,m;
    scanf("%d %d", &h, &m);
    
    if(h == 0){
        
        if(m >= 45){
            h = h;
            m = m - 45;
            printf("%d %d\n", h, m);
        }
        else{
            h = h + 23;
            m = m + 15;
            printf("%d %d\n", h, m);
        }
    }
    
    else{
        
        if(m >= 45){
            m = m -45;
            printf("%d %d\n", h, m);
        }
        
        else{
            h = h - 1;
            m = m + 15;
            printf("%d %d\n", h, m);
        }
    }
    
    return 0;
}
