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
//	string expr;
//
//	int cnt;
//	for (int i = 0; i < n; i++) {
//		cin >> expr;
//		cnt = 0;
//		for (char c : expr) {
//			if (c == '(') {
//				cnt++;
//			}
//			else {
//				if (cnt == 0) {
//					cnt = -1;
//					break;
//				}
//				else {
//					cnt--;
//				}
//			}
//		}
//
//		if (cnt == 0) {
//			cout << "YES\n";
//		}
//		else {
//			cout << "NO\n";
//		}
//	}
//
//	return 0;
//}