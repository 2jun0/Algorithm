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
//	int n, k;
//	cin >> n >> k;
//
//	int f = 1;
//	for (int i = n - k + 1; i <= n; i++) {
//		f *= i;
//	}
//
//	for (int i = 2; i <= k; i++) {
//		f /= i;
//	}
//
//	cout << f;
//
//	return 0;
//}