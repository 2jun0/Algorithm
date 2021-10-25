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
//long long powMod(int n, int k, int mod) {
//	if (k == 0) {
//		return 1;
//	}
//
//	long long temp = powMod(n, k / 2, mod);
//	long long temp2 = (temp * temp) % mod;
//
//	if (k % 2 == 0) {
//		return temp2;
//	}
//	else {
//		return (temp2 * n) % mod;
//	}
//}
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int T;
//	cin >> T;
//	for (int t = 0; t < T; t++)	{
//		int a, b;
//		cin >> a >> b;
//		int result = powMod(a, b, 10);
//		result = (result == 0) ? 10 : result;
//		cout <<  result<< '\n';
//	}
//
//	return 0;
//}