// 11931 수 정렬하기4

#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
	// your code goes here
	int N;
	cin >> N;
	int arr[1000001];
	for(int i = 0; i < N; i++){
		cin >> arr[i];

	}
	sort(arr,arr+N,greater<int>());
	
	for(int i = 0; i < N; i++){
		cout << arr[i] << "\n";
	}
	return 0;
}