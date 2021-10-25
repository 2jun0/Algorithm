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
//	int a, b;
//	cin >> a >> b;
//
//	int minV = min(a, b);
//	int maxV = max(a, b);
//
//	for (int i = minV; i >= 1; i--) {
//		if (a % i == 0 && b % i == 0) {
//			cout << i << '\n';
//			break;
//		}
//	}
//
//	for (int i = maxV;; i += maxV) {
//		if (i % a == 0 && i % b == 0) {
//			cout << i << '\n';
//			break;
//		}
//	}
//
//	return 0;
//}