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
//int gcd(int a, int b) {
//	int n, temp;
//	if (a < b) {
//		SWAP(a, b, temp);
//	}
//
//	while (b != 0) {
//		n = a % b;
//		a = b;
//		b = n;
//	}
//
//	return a;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N;
//	cin >> N;
//
//	int pre, cur;
//	cin >> pre;
//	int a = 1, b = 1, gcdV;
//	for (int i = 1; i < N; i++, pre = cur) {
//		cin >> cur;
//		a *= pre;
//		b *= cur;
//
//		gcdV = gcd(a, b);
//		a /= gcdV;
//		b /= gcdV;
//
//		cout << a << '/' << b << '\n';
//	}
//
//	return 0;
//}