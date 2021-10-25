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
//int func(int* nums, int N, int idx, int sum, float contain, int s) {
//	if(contain) sum += nums[idx];
//
//	if (idx == N - 1) {
//		if (sum == s) return 1;
//		else return 0;
//	}
//
//	return func(nums, N, idx + 1, sum, false, s) + func(nums, N, idx + 1, sum, true, s);
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int N, S;
//	cin >> N >> S;
//
//	int* nums = new int[N];
//	for (int i = 0; i < N; i++) {
//		cin >> nums[i];
//	}
//
//	int result = func(nums, N, 0, 0, false, S) + func(nums, N, 0, 0, true, S);
//	if (S == 0) result--;
//	cout << result;
//
//	delete[] nums;
//
//	return 0;
//}