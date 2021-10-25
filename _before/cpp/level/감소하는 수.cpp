//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
//#include <set>
//#include <queue>
//#include <map>
//
//#define ABS(x) (((x) < 0)?-(x):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int N;
//	cin >> N;
//
//	stack<int> s;
//	stack<int> save_s;
//	s.push(0);
//	for (int i = 0; i < N; i++) {
//		int k;
//		for (k = 0; k <= 9; k++) {
//			int cur = s.top();
//			s.pop();
//			if (s.empty()) {
//				if (cur + 1 >= 10) {
//					s.push(k+1);
//					save_s.push(k);
//				}
//				else {
//					s.push(cur + 1);
//				}
//				break;
//			}
//			int next = s.top();
//			if (cur + 1 >= next) {
//				save_s.push(k);
//			}
//			else {
//				s.push(cur + 1);
//				break;
//			}
//		}
//
//		if (k > 9) {
//			cout << -1;
//			return 0;
//		}
//
//		while (!save_s.empty()) {
//			int num = save_s.top();
//			save_s.pop();
//			s.push(num);
//		}
//	}
//
//	string result = "";
//	while (!s.empty()) {
//		if (s.top() >= 10) {
//			cout << -1;
//			return 0;
//		}
//
//		result = to_string(s.top()) + result;
//		s.pop();
//	}
//
//	cout << result;
//
//	return 0;
//}