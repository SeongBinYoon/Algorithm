// 1546 평균

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    float N,score,result;//N은 과목 개수, score는 둘째 줄 점수, result는 변환한 값
    float M = 0,x = 0;//M은 점수 중 최대값, x는 score의 합
    scanf("%f\n",&N);//N받기
    
    for(int i = 0; i < N; i++){//N만큼 돌림
        
        scanf("%f",&score);//score 받기
        x += score;//score 값 모두 더하기
        
        if(score > M){
            M = score;//최대값 갱신
        }
        
    }
    result = x * 100 / (M * N);//변환한 값
    
    printf("%f\n",result);
}
