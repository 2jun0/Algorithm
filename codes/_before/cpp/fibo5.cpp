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
//	for (int i = 2; i <= n; i ++) {
//		fn_temp = fn2;
//		fn2 = fn + fn2;
//		fn = fn_temp;
//	}
//
//	return fn2;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int n;
//	cin >> n;
//
//	cout << fibo(n);
//
//	return 0;
//}