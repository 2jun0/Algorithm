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
//int fiboMod(int n, int mod) {
//	int f1 = 0;
//	int f2 = 1;
//	int temp;
//
//	if (n == 0) {
//		return f1;
//	}
//
//	for (int i = 1; i < n; i++) {
//		temp = f2;
//		f2 = (f1 + f2)%mod;
//		f1 = temp;
//	}
//
//	return f2;
//}
//
//int getPisanoPeriod(int mod) {
//	int f1 = 0;
//	int f2 = 1;
//	int temp;
//
//	int p = 1;
//	while (true) {
//		temp = f2;
//		f2 = (f1 + f2) % mod;
//		f1 = temp;
//
//		if (f1 == 0 && f2 == 1) {
//			return p;
//		}
//
//		p++;
//	}
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	long long n;
//	cin >> n;
//	int p = getPisanoPeriod(1000000);
//	int result = fiboMod(n%p, 1000000);
//	cout << result;
//	return 0;
//}