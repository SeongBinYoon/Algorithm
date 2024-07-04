// 10430 나머지

#include <stdio.h>

int main(void) {
	// your code goes here
	int A,B,C;
	scanf("%d\n%d\n%d\n", &A, &B, &C);
	printf("%d\n", (A+B)%C);
	printf("%d\n", (A%C + B%C)%C);
	printf("%d\n", (A*B)%C);
	printf("%d\n", (A%C * B%C)%C);
	return 0;
}