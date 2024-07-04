// 14681 사분면 고르기

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    int x,y;
    scanf("%d\n%d",&x,&y);
    
    if(x > 0 && y > 0){
        printf("1\n");
    }
    else if(x < 0 && y > 0){
        printf("2\n");
    }
    else if(x < 0 && y < 0){
        printf("3\n");
    }
    else if(x > 0 && y < 0){
        printf("4\n");
    }
    return 0;
}
