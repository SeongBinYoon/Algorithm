// 9086 문자열

#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	string a,b,c;
	for(int i = 0; i < n; i++){
		cin >> a;
		b = a[0];
		c = a[a.length()-1];
		cout << b + c << "\n";
	}
}