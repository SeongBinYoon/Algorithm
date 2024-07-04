// 10807 개수 세기

#include <stdio.h>

int main(void) {
	int N;
	int i;
	int k;
	int l;
	int m;
	int A[100]={0,};
	scanf("%d",&N);
	int sum =0;
	for(int i=0;i<N;i++){
		int k;
		scanf("%d",&k);
		A[i]=k;
	}
	for(int i=0;i<N;i++){
		scanf("%d",&l);
		if (A[i] == l){
			sum++; //sum=sum+1;
		}
	}
	printf("%d",sum);
	
	
	
	return 0;
}