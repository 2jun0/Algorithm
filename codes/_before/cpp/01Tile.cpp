//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
//
//#define MAX(x,y) (((x) < (y))?(y):(x))
//#define ABS(x) (((x) < 0)?-(x):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//long long getCnt(long long n) {
//	/*int total = 0,  cnt, temp;
//	for (int zCnt = 0; zCnt <= n/2; zCnt++) {
//		temp = 1;
//		cnt = n - zCnt;
//
//		for (int i = zCnt + 1; i <= cnt; i++) {
//			temp *= i;
//		}
//
//		for (int i = 2; i <= cnt - zCnt; i++) {
//			temp /= i;
//		}
//
//		total += temp;
//	}
//
//	return total;*/
//
//	long long fn = 1;
//	long long fn2 = 2;
//	long long temp;
//
//	if (n == 1) {
//		return fn;
//	}
//
//	for (long long i = 2; i < n; i++) {
//		temp = fn2;
//		fn2 = (fn + fn2) % 15746;
//		fn = temp;
//	}
//
//	return fn2;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	long long n;
//	cin >> n;
//
//	cout << getCnt(n);
//
//	return 0;
//}