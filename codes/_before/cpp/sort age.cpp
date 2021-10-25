//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//
//#define MIN(x,y) ((x > y)?(y):(x))
//#define MAX(x,y) ((x < y)?(y):(x))
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
//	Y*sortedY;
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
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N;
//	cin >> N;
//
//	int* ages = new int[N];
//	string* names = new string[N];
//
//	for (int i = 0; i < N; i++) {
//		cin >> ages[i] >> names[i];
//	}
//
//	mergeSort(ages, names, 0, N - 1);
//
//	for (int i = 0; i < N; i++) {
//		cout << ages[i] << ' ' << names[i] << '\n';
//	}
//
//	return 0;
//}