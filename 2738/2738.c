// 2738 행렬 덧셈

#include <stdio.h>

int main(void) {
	int A[100][100]={0,};
	int B[100][100]={0,};
	int N;
	int M;
	scanf("%d %d", &N, &M);
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++){
			scanf("%d",&A[i][j]);
		}
	}
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++){
			scanf("%d",&B[i][j]);
		}
	}
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++){
			printf("%d ",A[i][j]+B[i][j]);
		}
		printf("\n");
	}
	
	return 0;
}