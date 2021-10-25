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
//	long long n, m;
//	cin >> n >> m;
//
//	long long cntOf2 = 0;
//	long long cntOf5 = 0;
//
//	for (long long i = 2; i <= n; i *= 2) {
//		cntOf2 += n / i;
//	}
//
//	for (long long i = 2; i <= (n - m); i *= 2) {
//		cntOf2 -= (n - m) / i;
//	}
//
//	for (long long i = 2; i <= m; i *= 2) {
//		cntOf2 -= m / i;
//	}
//
//	for (long long i = 5; i <= n; i *= 5) {
//		cntOf5 += n / i;
//	}
//
//	for (long long i = 5; i <= (n - m); i *= 5) {
//		cntOf5 -= (n - m) / i;
//	}
//
//	for (long long i = 5; i <= m; i *= 5) {
//		cntOf5 -= m / i;
//	}
//
//	cout << min(cntOf2, cntOf5);
//
//	return 0;
//}