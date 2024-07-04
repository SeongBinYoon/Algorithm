// 9316 Hello Judge

#include <stdio.h>

void func(int N) {
	for(int i=0; i<N; i++){
		printf("Hello World, Judge %d!\n",i+1);
	} 
	
}

int main(){
	int N;
	scanf("%d", &N);
	func(N);
}