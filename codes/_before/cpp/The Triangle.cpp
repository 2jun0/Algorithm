//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
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
//	int n;
//	cin >> n;
//
//	int** nums = new int*[n];
//
//	for (int i = 0; i < n; i++) {
//		nums[i] = new int[i+1];
//		for (int j = 0; j <= i; j++) {
//			cin >> nums[i][j];
//		}
//	}
//
//	for (int i = 1; i < n; i++) {
//		for (int j = 0; j <= i; j++) {
//			if (j == 0) {
//				// first
//				nums[i][j] += nums[i - 1][0];
//			}
//			else if (j == i) {
//				// end
//				nums[i][j] += nums[i - 1][i - 1];
//			}
//			else {
//				nums[i][j] += max(nums[i - 1][j-1], nums[i - 1][j]);
//			}
//		}
//	}
//
//	int maxVal = 0;
//	for (int i = 0; i < n; i++) {
//		maxVal = max(maxVal, nums[n - 1][i]);
//	}
//
//	cout << maxVal;
//
//	return 0;
//}