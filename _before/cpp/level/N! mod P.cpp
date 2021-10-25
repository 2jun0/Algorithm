//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//
//#define MIN(x,y) ((x > y)?(y):(x))
//#define MAX(x,y) ((x < y)?(y):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//template <typename T>
//T factorialMod(T xStart, T xEnd, T b) {
//	if (xStart == xEnd) return xStart % b;
//	// 1ma * 2ma  3
//	T mid = (xStart + xEnd) / 2;
//	return (factorialMod(xStart, mid, b) * factorialMod(mid + 1, xEnd, b)) % b;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	long long N, P;
//	cin >> N >> P;
//
//	cout << factorialMod(1LL, N, P);
//
//	return 0;
//}
