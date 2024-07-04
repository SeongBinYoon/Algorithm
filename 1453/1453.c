// 1453 피시방 알바

#include <stdio.h>

int main(void) {
	int N;
	int A[101]={0,};
	scanf("%d",&N);
	int sum = 0;
	for(int i=0;i<N;i++){
		int k;
		scanf("%d",&k);
		A[k]+=1;
	}
	for(int i=0;i<101;i++){
		if(A[i]>1){
			sum = sum + A[i] - 1;
		}
	}
	printf("%d",sum);
	
	return 0;
}