// 10866 덱

#include <deque>
#include <iostream>
#include <stack>
using namespace std;

deque<int> dq;

int main() {
	
	int n; cin >> n;
	
	while(n--){
		string s; cin >> s;
		if(s == "push_front") {
			int x; cin >> x;
			dq.push_front(x);
			
		}
		else if(s == "push_back"){
			int x; cin >> x;
			dq.push_back(x);
		}
		else if(s == "pop_front"){
			cout << (dq.empty() ? -1 : dq.front()) << '\n';
			if(dq.empty() == false) dq.pop_front();
			
			
		}
		else if(s == "pop_back"){
			cout << (dq.empty() ? -1 : dq.back()) << '\n';
			if(dq.empty() == false) dq.pop_back();;
			
		}
		else if(s == "front") cout << (dq.empty() ? -1 : dq.front()) << '\n';
			
		else if(s == "back") cout << (dq.empty() ? -1 : dq.back()) << '\n';
			
		else if(s == "size") cout << dq.size() << '\n';
			
		else if(s == "empty") cout << (dq.empty() ? 1 : 0) << '\n';

	}
	return 0;
}