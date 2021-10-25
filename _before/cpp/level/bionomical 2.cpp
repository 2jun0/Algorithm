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
//int _bino(int n, int r, int** memo) {
//	if (r == 0 || n == r) {
//		return 1;
//	}
//	else if (memo[n][r] != -1) {
//		return memo[n][r];
//	}
//	else {
//		return (memo[n][r] = (_bino(n - 1, r, memo) % 10007 + _bino(n - 1, r - 1, memo) % 10007) % 10007);
//	}
//}
//
//int bino(int n, int r) {
//	int** memo = new int* [n+1];
//	for (int i = 0; i < n+1; i++) {
//		memo[i] = new int[r+1];
//		memset(memo[i], -1, sizeof(int) * (r+1));
//	}
//
//	return _bino(n,r, memo);
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N, K;
//	cin >> N >> K;
//
//	cout << bino(N, K);
//
//	return 0;
//}