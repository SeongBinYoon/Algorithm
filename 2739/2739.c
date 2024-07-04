// 2739 구구단

#include <stdio.h>

void func(int N) {
	for(int i=1; i<10; i++){
		printf("%d * %d = %d\n", N,i,(N*i) );
	} 
	
}

int main(){
	int N;
	scanf("%d", &N);
	func(N);
}