// 11656 접미사 배열

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	vector<string> arr;
	string a;
	cin >> a;
	for(int i = 0; i < a.size(); ++i){
		string tmp = a.substr(i,a.size()-i);
		arr.push_back(tmp);
	}
	sort(arr.begin(),arr.end());
	
	for(int i = 0; i < arr.size(); i++){
		cout << arr[i] << "\n";
	}
}