// 10845 큐

#include <iostream>
#include <queue>
using namespace std;

int main() {
   ios::sync_with_stdio(0); cin.tie(0);
   int n; cin >> n;
   queue<int> q;
   while (n--) {
      string s; cin >> s;
      if (s == "push") {
         int x; cin >> x;
         q.push(x);
      } else if (s == "pop") {
         if (q.empty()) cout << -1 << '\n';
         else {
            cout << q.front() << '\n';
            q.pop();
         }
      }
      else if (s == "size")
         cout << q.size() << '\n';
      else if (s == "empty")
         cout << q.empty() << '\n';
      else if (s == "front")
         cout << (q.empty() ? -1 : q.front()) << '\n';
      else cout << (q.empty() ? -1 : q.back()) << '\n';
   }
   return 0;
}