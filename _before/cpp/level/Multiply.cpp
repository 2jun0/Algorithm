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
//int powMod(int n, int k, int m) {
//	if (k == 0) {
//		return 1;
//	}
//
//	long long temp  = powMod(n, k / 2, m);
//	long long temp2 = (temp * temp) % m;
//
//	if (k % 2 == 0) {
//		return temp2;
//	}
//	else {
//		return (temp2 * (n % m)) % m;
//	}
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int A, B, C;
//	cin >> A >> B >> C;
//
//	cout << powMod(A, B, C);
//
//	return 0;
//}