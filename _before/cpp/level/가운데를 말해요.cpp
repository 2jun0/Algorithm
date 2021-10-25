//#include <iostream>
//#include <cstring>
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
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int N;
//	cin >> N;
//
//	priority_queue<int, vector<int>, less<int>> left;
//	priority_queue<int, vector<int>, greater<int>> right;
//
//	int num;
//	cin >> num;
//	left.push(num);
//	cout << num << '\n';
//
//	for (int _ = 1; _ < N; _++) {
//		int num;
//		cin >> num;
//
//		if (left.top() >= num) {
//			left.push(num);
//
//			while (left.size() > right.size()+1) {
//				right.push(left.top());
//				left.pop();
//			}
//		}
//		else {			
//			right.push(num);
//
//			while (right.size() > left.size()) {
//				left.push(right.top());
//				right.pop();
//			}
//		}
//
//		cout << left.top() << '\n';
//	}
//
//	return 0;
//}