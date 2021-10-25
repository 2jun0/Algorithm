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
//	long long minV, maxV;
//	cin >> minV >> maxV;
//
//	bool* nums = new bool[maxV - minV + 1];
//	memset(nums, false, sizeof(bool)*(maxV - minV + 1));
//
//	for (long long i = 2; i * i <= maxV; i++) {
//		long long powV = i * i;
//
//		long long x = (minV / powV) * powV;
//		if (minV > x) {
//			x += powV;
//		}
//
//		while (x <= maxV) {
//			nums[x - minV] = true;
//			x += powV;
//		}
//	}
//
//	int cnt = 0;
//	for (int i = 0; i <= maxV-minV; i++) {
//		if (!nums[i]) cnt++;
//	}
//
//	cout << cnt;
//
//	delete[] nums;
//
//	return 0;
//}