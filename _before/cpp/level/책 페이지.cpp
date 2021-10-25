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
//void addCnt(vector<int> &cnt, int num, int k) {
//	while (num > 0) {
//		cnt[num % 10] += k;
//		num /= 10;
//	}
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	vector<int> cnt(10);
//	int A = 1, N;
//	int k = 1;
//	cin >> N;
//
//	while (N > 0) {
//		while (N % 10 != 9 && N >= A) {
//			addCnt(cnt, N--, k);
//		}
//
//		while (A % 10 != 0 && N >= A) {
//			addCnt(cnt, A++, k);
//		}
//
//		if (N < A) {
//			break;
//		}
//
//
//		N /= 10;
//		A /= 10;
//
//		for (int i = 0; i <= 9; i++) {
//			cnt[i] += (N - A + 1) * k;
//		}
//
//		k *= 10;
//	}
//
//	for (int c : cnt) {
//		cout << c << ' ';
//	}
//
//	return 0;
//}