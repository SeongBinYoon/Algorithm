// 9012 괄호

#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main(){
    int t;
    cin >> t;

    while(t--){
        string a;
        cin >> a;

        stack<char> s;

        bool vps = true;
        for(int i=0; i<a.size(); i++){
            if(a[i] == '(') s.push('(');
            else{ //닫는 괄호
                if(s.empty()){
                    vps = false;
                    break;
                }
                else s.pop();
            }
        }

        if(!s.empty()) vps = false;

        if(vps) cout << "YES\n";
        else cout << "NO\n"; 
    }
}