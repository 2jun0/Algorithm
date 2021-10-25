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
//void mergeSort(T* arr, int start, int end, bool isAscending = true) {
//	int mid = (start + end) / 2;
//	T* sorted;
//	int s = 0;
//	int i = start, j = mid + 1;
//
//	if (start < end) {
//		mergeSort(arr, start, mid, isAscending);
//		mergeSort(arr, mid + 1, end, isAscending);
//
//		sorted = new T[end - start + 1];
//
//		while (i <= mid && j <= end) {
//			if (isAscending) {
//				if (arr[i] <= arr[j]) {
//					sorted[s] = arr[i];
//					i++;
//				}
//				else {
//					sorted[s] = arr[j];
//					j++;
//				}
//				s++;
//			}
//			else {
//				if (arr[i] >= arr[j]) {
//					sorted[s] = arr[i];
//					i++;
//				}
//				else {
//					sorted[s] = arr[j];
//					j++;
//				}
//				s++;
//			}
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
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N;
//	cin >> N;
//	string str = to_string(N);
//	char* arr = new char[str.size()];
//	
//	for (int i = 0; i < str.size(); i++) {
//		arr[i] = str[i];
//	}
//
//	mergeSort(arr, 0, str.size() - 1, false);
//
//	for (int i = 0; i < str.size(); i++) {
//		cout << arr[i];
//	}
//
//	return 0;
//}