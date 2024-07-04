// 10828 스택

#include <iostream>
#include <stack>
using namespace std;

int main() {
    
   int n; cin >> n;
   stack<int> st;

   while (n--) {
      string s; cin >> s;
      if (s == "push") {
         int x; cin >> x;
         st.push(x);
      }
      else if (s == "top")
         cout << (st.empty() ? -1 : st.top()) << '\n';
      else if (s == "size")
         cout << st.size() << '\n';
      else if (s == "empty")
         cout << st.empty() << '\n';
      else {
         if (st.empty()) cout << -1 << '\n';
         else {
            cout << st.top() << '\n';
            st.pop();
         }
      }
   }
   return 0;
}