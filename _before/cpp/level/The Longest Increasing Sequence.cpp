//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
//#include <set>
//
//#define ABS(x) (((x) < 0)?-(x):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//int downstairs(int*nums, int n, int start, int* maxNumOfSeq, int startSeq) {
//	if (start >= n) {
//		return startSeq+1;
//	}
//
//	int maxSeq = startSeq;
//
//	for (int i = start; i < n; i++) {
//
//		// new seq
//		if (maxNumOfSeq[maxSeq] > nums[i]) {
//			maxNumOfSeq[maxSeq + 1] = nums[i];
//			maxSeq++;
//			continue;
//		}
//
//		int k;
//		for (k = maxSeq - 1; k >= startSeq; k--) {
//			// the seq exists
//			if (maxNumOfSeq[k] > nums[i]) {
//				maxNumOfSeq[k + 1] = max(maxNumOfSeq[k + 1], nums[i]);
//				break;
//			}
//		}
//
//		if (k == startSeq-1) {
//			maxNumOfSeq[startSeq] = max(maxNumOfSeq[startSeq], nums[i]);
//		}
//	}
//
//	return maxSeq + 1;
//}
//
//int upstairs(int* nums, int n, int end, int *minNumOfSeq) {
//	int maxSeq = 0;
//	minNumOfSeq[maxSeq] = nums[0];
//
//	if (end <= 0) {
//		return 0;
//	}
//
//	for (int i = 1; i < end; i++) {
//		
//		// new seq
//		if (minNumOfSeq[maxSeq] < nums[i]) {
//			minNumOfSeq[maxSeq + 1] = nums[i];
//			maxSeq++;
//			continue;
//		}
//
//		int k;
//		for (k = maxSeq - 1; k >= 0; k--) {
//			// the seq exists
//			if (minNumOfSeq[k] < nums[i]) {
//				minNumOfSeq[k + 1] = min(minNumOfSeq[k + 1], nums[i]);
//				break;
//			}
//		}
//
//		if (k == -1) {
//			minNumOfSeq[0] = min(minNumOfSeq[0], nums[i]);
//		}
//	}
//
//	return maxSeq + 1;
//}
//
//int getMaxSeq(int* nums, int n) {
//	int maxResult = 0;
//	int seqCnt;
//	int* numOfSeq = new int[n];
//
//	for (int i = 0; i <= n; i++) {
//		seqCnt = upstairs(nums, n, i, numOfSeq);
//		maxResult = max(
//			maxResult, 
//			downstairs(nums, n, i, numOfSeq, seqCnt-1)
//		);
//	}
//
//	return maxResult;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int n;
//	cin >> n;
//
//	int* nums = new int[n];
//	for (int i = 0; i < n; i++) {
//		cin >> nums[i];
//	}
//
//	cout << getMaxSeq(nums, n);
//}