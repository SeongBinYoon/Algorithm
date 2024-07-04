// 10987 모음의 개수

#include <stdio.h>
#include <string.h>

int letter(char N[100]){
	int sum = 0;
	for(int i=0;i<strlen(N);i++){
		if(N[i] == 'a' || N[i] == 'e' || N[i] == 'i' || N[i] == 'o' || N[i] == 'u'){
			sum += 1;
		}
	}
	return sum;
}



int main() {
	char N[100];
	scanf("%s",&N);
	printf("%d", letter(N));
}