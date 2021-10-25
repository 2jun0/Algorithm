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
//	long long fn = 1;
//	long long fn2 = 1;
//	long long fn3 = 1;
//	long long fn_temp;
//	long long fn_temp2;
//
//	if (n == 1) {
//		return fn;
//	}
//	else if (n == 2) {
//		return fn2;
//	}
//
//	for (int i = 4; i <= n; i++) {
//		fn_temp = fn3;
//		fn3 = fn + fn2;
//		fn_temp2 = fn2;
//		fn2 = fn_temp;
//		fn = fn_temp2;
//	}
//
//	return fn3;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int n;
//	int temp;
//	cin >> n;
//
//	for (int i = 0; i < n; i++) {
//		cin >> temp;
//		cout << fibo(temp) << '\n';
//	}
//
//	return 0;
//}