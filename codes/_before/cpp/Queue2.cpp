//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
//#include <set>
//#include <queue>
//
//#define ABS(x) (((x) < 0)?-(x):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(NULL);
//
//	queue<int> q;
//
//	int N;
//	cin >> N;
//
//	string s;
//	int param;
//	for (int i = 0; i < N; i++)
//	{
//		cin >> s;
//
//		if (s.compare("push") == 0) {
//			cin >> param;
//			q.push(param);
//		}
//		else if (s.compare("front") == 0) {
//			if (q.empty()) {
//				cout << "-1\n";
//			}
//			else {
//				cout << q.front() << '\n';
//			}
//		}
//		else if (s.compare("size") == 0) {
//			cout << q.size() << '\n';
//		}
//		else if (s.compare("back") == 0) {
//			if (q.empty()) {
//				cout << "-1\n";
//			}
//			else {
//				cout << q.back() << '\n';
//			}
//		}
//		else if (s.compare("empty") == 0) {
//			cout << (q.empty()?1:0) << '\n';
//		}
//		else if (s.compare("pop") == 0) {
//			if (q.empty()) {
//				cout << "-1\n";
//			}
//			else {
//				cout << q.front() << '\n';
//				q.pop();
//			}
//		}
//	}
//
//	return 0;
//}