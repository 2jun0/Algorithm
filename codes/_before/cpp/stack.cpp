//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
//#include <set>
//
//#define ABS(x) (((x) < 0)?-(x):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int n;
//	cin >> n;
//
//	string cmd;
//	int param;
//
//	stack<int> stk;
//
//	for (int i = 0; i < n; i++) {
//		cin >> cmd;
//
//		if (cmd.compare("push") == 0) {
//			cin >> param;
//			stk.push(param);
//		}
//		else if (cmd.compare("pop") == 0) {
//			if (stk.empty()) {
//				cout << -1 << '\n';
//			}
//			else {
//				cout << stk.top() << '\n';
//				stk.pop();
//			}
//		}
//		else if (cmd.compare("top") == 0) {
//			if (stk.empty()) {
//				cout << -1 << '\n';
//			}
//			else {
//				cout << stk.top() << '\n';
//			}
//		}
//		else if (cmd.compare("size") == 0) {
//			cout << stk.size() << '\n';
//		}
//		else if (cmd.compare("empty") == 0) {
//			if (stk.empty()) {
//				cout << 1 << '\n';
//			}
//			else {
//				cout << 0 << '\n';
//			}
//		}
//	}
//
//	return 0;
//}