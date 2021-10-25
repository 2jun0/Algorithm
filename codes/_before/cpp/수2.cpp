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
//	int L;
//	cin >> L;
//	
//	vector<int> luckySet(L);
//	for (int i = 0; i < L; i++) {
//		cin >> luckySet[i];
//	}
//	sort(luckySet.begin(), luckySet.end());
//
//	int N;
//	cin >> N;
//	for (int i = 0; i < L; i++) {
//		if (N == luckySet[i]) {
//			cout << 0;
//			return 0;
//		}
//		else if (N < luckySet[i]) {
//			int front = (i == 0) ? 1 : luckySet[i - 1] + 1;
//			int back = luckySet[i] - 1;
//			cout << (N - front + 1) * (back - N + 1) - 1;
//			return 0;
//		}
//	}
//
//	return 0;
//}