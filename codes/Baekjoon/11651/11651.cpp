// 11651 좌표 정렬하기2

#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

int main() {
	
	vector< pair<int,int> > v;
	
	int n;
	cin >> n;
	for(int i = 0; i < n; i++){
		int x,y;
		cin >> x >> y;	
		v.push_back(make_pair(y,x));
	}
	sort(v.begin(),v.end());
	
	for(int i = 0; i < v.size(); i++){
		cout << v[i].second << " " << v[i].first << "\n";
	}
	
	
	return 0;
}