// 1436 영화감독 숌

#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	int num = 666;
	int cnt = 0;
	while(1){
		if(cnt == n) break;
		int k = num, flag = 0;
		while(k > 0){
			if(k % 1000 == 666) flag = 1;
			k /= 10;
		}
		if(flag == 1) cnt ++;
		num ++;
	}
	cout << num - 1;
}