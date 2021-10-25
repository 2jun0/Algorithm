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
//void getZIdx(int startIdx, int start_x, int end_x, int start_y, int end_y, int& c, int& r, int& result) {
//	int mid_x = (start_x + end_x) / 2;
//	int mid_y = (start_y + end_y) / 2;
//	if (start_x == end_x) {
//		if (mid_x == c && mid_y == r) {
//			result = startIdx;
//		}
//		return;
//	}
//
//	int size = (end_x - start_x + 1) * (end_y - start_y + 1) / 4;
//	if (c <= mid_x) {
//		if (r <= mid_y) {
//			getZIdx(startIdx, start_x, mid_x, start_y, mid_y, c, r, result);
//		}
//		else {
//			getZIdx(startIdx + size * 2, start_x, mid_x, mid_y + 1, end_y, c, r, result);
//		}
//	}
//	else {
//		if (r <= mid_y) {
//			getZIdx(startIdx+size, mid_x + 1, end_x, start_y, mid_y, c, r, result);
//		}
//		else {
//			getZIdx(startIdx+size*3, mid_x + 1, end_x, mid_y + 1, end_y, c, r, result);
//		}
//	}
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int N, r, c;
//	cin >> N >> r >> c;
//
//	int result;
//	getZIdx(0, 0, (1 << N) - 1, 0, (1 << N) - 1, c, r, result);
//
//	cout << result;
//
//	return 0;
//}