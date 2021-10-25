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
//long long fibo(int n) {
//	long long fn = 0;
//	long long fn2 = 1;
//	long long fn_temp;
//
//	if (n == 0) {
//		return fn;
//	}
//
//	for (int i = 2; i <= n; i++) {
//		fn_temp = fn2;
//		fn2 = fn + fn2;
//		fn = fn_temp;
//	}
//
//	return fn2;
//}
//
//void predict0and1(int n) {
//	int cntZ = 1;
//	int cntF = 0;
//	int cnt2Z = 0;
//	int cnt2F = 1;
//	int cnt_tempZ;
//	int cnt_tempF;
//
//	if (n == 0) {
//		cout << cntZ << ' ' << cntF;
//		return;
//	}
//
//	for (int i = 2; i <= n; i++) {
//		cnt_tempZ = cnt2Z;
//		cnt_tempF = cnt2F;
//		cnt2Z = cntZ + cnt2Z;
//		cnt2F = cntF + cnt2F;
//		cntZ = cnt_tempZ;
//		cntF = cnt_tempF;
//	}
//
//	cout << cnt2Z << ' ' << cnt2F;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int n, temp;
//	cin >> n;
//
//	for (int i = 0; i < n; i++) {
//		cin >> temp;
//		predict0and1(temp);
//		cout << '\n';
//	}
//
//	return 0;
//}