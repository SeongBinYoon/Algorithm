// 10872 팩토리얼

#include <stdio.h>
int fac(int N){
	int acc = 1;
	for(int i=1;i<=N; i++) acc*=i;
	return acc;
}



int main() {
	int N;
	scanf("%d", &N);
	printf("%d",fac(N));
}