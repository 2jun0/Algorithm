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
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N, K;
//	cin >> N >> K;
//
//	int* coins = new int[N];
//	for (int i = 0; i < N; i++) {
//		cin >> coins[i];
//	}
//
//	int sum = 0, cnt = 0;
//
//	for (int i = N-1; i >= 0; i--) {
//		while (K >= sum + coins[i]) {
//			sum += coins[i];
//			cnt++;
//		}
//	}
//
//	cout << cnt;
//
//	return 0;
//}