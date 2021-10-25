//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
//
//#define MIN(x,y) ((x > y)?(y):(x))
//#define MAX(x,y) ((x < y)?(y):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//const int EXETREME_MIN = -1000000000;
//const int EXETREME_MAX = 1000000000;
//int getMaxNum(int* nums, int depth, int plus, int minus, int mul, int div) {
//	if (depth == 0) {
//		return nums[depth];
//	}
//
//	int temp1 = (plus)?(getMaxNum(nums, depth - 1, plus - 1, minus, mul, div) + nums[depth]):EXETREME_MIN;
//	int temp2 = (minus)?(getMaxNum(nums, depth - 1, plus, minus - 1, mul, div) - nums[depth]):EXETREME_MIN;
//	int temp3 = (mul)?(getMaxNum(nums, depth - 1, plus, minus, mul - 1, div) * nums[depth]):EXETREME_MIN;
//	int temp4 = (div)?(getMaxNum(nums, depth - 1, plus, minus, mul, div - 1) / nums[depth]):EXETREME_MIN;
//
//	return MAX(MAX(temp1, temp2), MAX(temp3, temp4));
//}
//
//int getMinNum(int* nums, int depth, int plus, int minus, int mul, int div) {
//	if (depth == 0) {
//		return nums[depth];
//	}
//
//	int temp1 = (plus) ? (getMinNum(nums, depth - 1, plus - 1, minus, mul, div) + nums[depth]) : EXETREME_MAX;
//	int temp2 = (minus) ? (getMinNum(nums, depth - 1, plus, minus - 1, mul, div) - nums[depth]) : EXETREME_MAX;
//	int temp3 = (mul) ? (getMinNum(nums, depth - 1, plus, minus, mul - 1, div) * nums[depth]) : EXETREME_MAX;
//	int temp4 = (div) ? (getMinNum(nums, depth - 1, plus, minus, mul, div - 1) / nums[depth]) : EXETREME_MAX;
//
//	return MIN(MIN(temp1, temp2), MIN(temp3, temp4));
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N;
//	cin >> N;
//
//	int* nums = new int[N];
//	for (int i = 0; i < N; i++) {
//		cin >> nums[i];
//	}
//
//	int plus, minus, mul, div;
//	cin >> plus >> minus >> mul >> div;
//
//	cout << getMaxNum(nums, N - 1, plus, minus, mul, div) << '\n' << getMinNum(nums, N - 1, plus, minus, mul, div);
//
//	return 0;
//}