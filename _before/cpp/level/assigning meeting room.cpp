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
//template<typename T>
//void mergeSort(T* arr, int start, int end, bool isAscending = true, bool (*cmp)(T&, T&) = _defaultCmp) {
//	int mid = (start + end) / 2;
//	T* sorted;
//	int s = 0, i = start, j = mid + 1;
//
//	if (start < end) {
//		mergeSort(arr, start, mid, isAscending, cmp);
//		mergeSort(arr, mid + 1, end, isAscending, cmp);
//
//		sorted = new T[end - start + 1];
//
//		while (i <= mid && j <= end) {
//			if (cmp(arr[i], arr[j]) == isAscending) {
//				sorted[s] = arr[i];
//				i++;
//			}
//			else {
//				sorted[s] = arr[j];
//				j++;
//			}
//			s++;
//		}
//
//		while (i <= mid) {
//			sorted[s] = arr[i];
//			i++;  s++;
//		}
//
//		while (j <= end) {
//			sorted[s] = arr[j];
//			j++;  s++;
//		}
//
//		for (int k = 0; k <= end - start; k++) {
//			arr[k + start] = sorted[k];
//		}
//
//		delete[] sorted;
//	}
//}
//
//template<typename T>
//bool meetingCmp(T& a, T& b) { 
//	if (a[0] == b[0]) {
//		return (a[1] <= b[1]);
//	}else return (a[0] <= b[0]); 
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N;
//	cin >> N;
//
//	int** meeting = new int* [N];
//
//	for (int i = 0; i < N; i++) {
//		meeting[i] = new int[2];
//		cin >> meeting[i][0] >> meeting[i][1];
//	}
//
//	mergeSort(meeting, 0, N - 1, true, meetingCmp);
//
//	int cnt = 0;
//	for (int i = 0, end = 0; i < N; i++) {
//		if (meeting[i][0] >= end) {
//			end = meeting[i][1];
//			cnt++;
//		}
//		else if (meeting[i][1] < end) {
//			end = meeting[i][1];
//		}
//	}
//
//	cout << cnt;
//
//	return 0;
//}