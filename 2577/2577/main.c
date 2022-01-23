//
//  main.c
//  2577
//
//  Created by SeongBinYoon on 2020/07/18.
//  Copyright © 2020 SeongBinYoon. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    int a,b,c,r;//a값,b값,c값,axbxc의 결과 r값
    int poarr[10] = {};//수를 넣을 배열 선언
    int cnt,rst;//r을 10으로 계속해서 나누어 나온 몫 저장소, r을 10으로 계속해서 나누고 마지막 남은 나머지 저장소
    int m = 0, sum = 0;//r의 길이를 구하기 위한 임시 몫 m , 길이 저장 변수 sum
    
    scanf("%d\n%d\n%d", &a,&b,&c);
    r = a * b * c;
    
    while(r >= 10){
        m = r / 10;
        r = m;
        sum += 1;
        
    }
    sum += 1;//r의 길이를 구하는 while loop
    
    r = a * b * c;
    for(int j = 0; j < sum; j++){
        cnt = r / 10;
        rst = r % 10;
        r = cnt;
        
        poarr[rst] += 1;
    }//10으로 연달아 나누어 나온 나머지값을 배열에 추가
    
    
    for(int l = 0; l < 10; l++){
        printf("%d\n", poarr[l]);
    }//배열 poarr 안에 있는 수 하나씩 꺼내서 printf
}
