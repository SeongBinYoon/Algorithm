// 5597 과제 안내신 분..?

#include <stdio.h>

int main(void) {
	int N;
	int A[31] = {0,};
	for(int i=1;i<29;i++){
		scanf("%d", &N);
		A[N] = 1;
	}
	for(int i=1; i<31; i++){
		if(A[i] == 0) printf("%d\n", i);
	}
	return 0;
}