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
//// Fn = (Fn-1 % b + Fn-2 % b) % b
//
//int getPisanoPeriod(int mod) {
//	int f1 = 0;
//	int f2 = 1;
//	int temp;
//
//	int p = 1;
//	while(true) {
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
//	int T;
//	cin >> T;
//
//	for (int t = 0; t < T; t++) {
//		int N, M;
//		cin >> N >> M;
//
//		cout << N << ' ' << getPisanoPeriod(M) << '\n';
//	}
//
//	return 0;
//}