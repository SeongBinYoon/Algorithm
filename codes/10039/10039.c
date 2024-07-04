// 10039 평균 점수

#include <stdio.h>

int main(void) {
	int i;
	int j;
	int avg = 0;
	int A[6] = {0,};
	for(int i=0; i<5; i++){
		scanf("%d", &A[i]);
	}
	for(int j=0;j<5;j++){
		if(A[j]<40) avg += 40;
		else avg += A[j];
	}
	
	printf("%d",avg/5);
	
	return 0;
}