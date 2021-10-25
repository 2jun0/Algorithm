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
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int T;
//	cin >> T;
//	for (int t = 0; t < T; t++) {
//		int N, M;
//		cin >> N >> M;
//		long long result = 1;
//		if (M - N > N) N = M - N;
//		for (int i = N+1; i <= M; i++) {
//			result *= i;
//		}
//		for (int i = M-N; i >= 1; i--) {
//			result /= i;
//		}
//		cout << result << '\n';
//	}
//
//	return 0;
//}