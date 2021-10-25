//#include <iostream>
//#include <cstring>
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
//		int src_x, src_y;
//		int dest_x, dest_y;
//		cin >> src_x >> src_y >> dest_x >> dest_y;
//
//		int N;
//		cin >> N;
//
//		int cnt = 0;
//		for (int i = 0; i < N; i++) {
//			long long c_x, c_y;
//			long long r;
//			cin >> c_x >> c_y >> r;
//			long long d = (c_x - src_x)* (c_x - src_x) + (c_y - src_y) * (c_y - src_y);
//			bool temp = false;
//			if (d < r*r) {
//				temp = !temp;
//			}
//			d = (c_x - dest_x) * (c_x - dest_x) + (c_y - dest_y) * (c_y - dest_y);
//			if (d < r*r) {
//				temp = !temp;
//			}
//
//			cnt += (int)temp;
//		}
//		cout << cnt << '\n';
//	}
//
//	return 0;
//}