// 2480 주사위 세 개

#include <stdio.h>

int main(void) {
	int a,b,c;
	
	scanf("%d %d %d", &a, &b, &c);
	
	if(a == b&& b == c){
		printf("%d\n", 10000+a*1000);
	}
	else if((a == b&&b != c) || (a == c&&c != b)){
		printf("%d\n", 1000+a*100);
	}
	else if(b == c&&c != a){
		printf("%d\n",1000+b*100);
	}
	else if(a != b && b != c && a != c){
		if(a < b && b < c){
			printf("%d\n", 100*c );
		}
		else if(a < c && c < b){
			printf("%d\n", 100*b);
		}
		else if(b < c && c < a){
			printf("%d\n", 100*a);
		}
		else if(b < a && a < c){
			printf("%d\n", 100*c);
		}
		else if(c < a && a < b){
			printf("%d\n", 100*b);
		}
		else if(c < b && b< a){
			printf("%d\n",100*a);
		}
	}
	
	
	
	return 0;
}