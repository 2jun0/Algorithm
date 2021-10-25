//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//
//#define MIN(x,y) ((x > y)?(y):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N, num;
//
//	cin >> N;
//
//	int cnt[10000];
//	memset(cnt, 0, sizeof(int) * 10000);
//
//	for (int i = 0; i < N; i++) {
//		cin >> num;
//		cnt[num - 1]++;
//	}
//
//	for (int i = 0; i < 10000; i++) {
//		if (cnt[i]) {
//			for (int j = 0; j < cnt[i]; j++) {
//				cout << i + 1 << '\n';
//			}
//		}
//	}
//
//	return 0;
//}