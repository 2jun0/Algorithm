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
//template<typename T>
//bool _defaultCmp(T& a, T& b) { return a <= b; }
//template<typename T, typename Y>
//void mergeSort(T* arr, Y* arrY, int start, int end, bool isAscending = true, bool (*cmp)(T&, T&) = _defaultCmp) {
//	int mid = (start + end) / 2;
//	T* sorted;
//	Y* sortedY;
//	int s = 0;
//	int i = start, j = mid + 1;
//
//	if (start < end) {
//		mergeSort(arr, arrY, start, mid, isAscending, cmp);
//		mergeSort(arr, arrY, mid + 1, end, isAscending, cmp);
//
//		sorted = new T[end - start + 1];
//		sortedY = new Y[end - start + 1];
//
//		while (i <= mid && j <= end) {
//			if (cmp(arr[i], arr[j]) == isAscending) {
//				sorted[s] = arr[i];
//				sortedY[s] = arrY[i];
//				i++;
//			}
//			else {
//				sorted[s] = arr[j];
//				sortedY[s] = arrY[j];
//				j++;
//			}
//			s++;
//		}
//
//		while (i <= mid) {
//			sorted[s] = arr[i];
//			sortedY[s] = arrY[i];
//			i++;  s++;
//		}
//
//		while (j <= end) {
//			sorted[s] = arr[j];
//			sortedY[s] = arrY[j];
//			j++;  s++;
//		}
//
//		for (int k = 0; k <= end - start; k++) {
//			arr[k + start] = sorted[k];
//			arrY[k + start] = sortedY[k];
//		}
//
//		delete[] sorted;
//		delete[] sortedY;
//	}
//}
//
//int getWireLineCnt(int* wiresLeft, int* wiresRight, int n) {
//	vector<pair<int, int>>* wireLineOfDepth = new vector<pair<int, int>>[n];
//	vector<pair<int, int>>::iterator iter;
//
//	int maxDepthIdx = 0;
//
//	wireLineOfDepth[0].push_back(make_pair(wiresLeft[0], wiresRight[0]));
//
//	for (int i = 1; i < n; i++) {
//
//		// Compare with current wire and former wires
//		bool isFound = false;
//		int k; 
//		for (k = maxDepthIdx; k >= 0; k--) {
//			for (iter = wireLineOfDepth[k].begin(); iter != wireLineOfDepth[k].end(); iter++) {
//				if (wiresRight[i] > iter->second) {
//					isFound = true;
//
//					wireLineOfDepth[k+1].push_back(make_pair(wiresLeft[i],wiresRight[i]));
//					if (k == maxDepthIdx) {
//						maxDepthIdx++;
//					}
//
//					break;
//				}
//			}
//
//			if (isFound) {
//				break;
//			}
//		}
//
//		if (k == -1) {
//			wireLineOfDepth[0].push_back(make_pair(wiresLeft[i], wiresRight[i]));
//		}
//	}
//
//	delete[] wireLineOfDepth;
//	return maxDepthIdx+1;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	
//	int n;
//	cin >> n;
//
//	int* wiresLeft = new int[n];
//	int* wiresRight = new int[n];
//
//	for (int i = 0; i < n; i++) {
//		cin >> wiresLeft[i] >> wiresRight[i];
//	}
//
//	mergeSort(wiresLeft, wiresRight, 0, n - 1);
//
//	cout << n - getWireLineCnt(wiresLeft, wiresRight, n);
//
//	return 0;
//}