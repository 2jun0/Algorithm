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
//template<typename T>
//void mergeSort(T* arr, int start, int end, bool isAscending = true, bool (*cmp)(T&, T&) = _defaultCmp) {
//	int mid = (start + end) / 2;
//	T* sorted;
//	int s = 0;
//	int i = start, j = mid + 1;
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
//bool stringCmp(string& a, string& b) {
//	if (a.size() == b.size()) {
//		return a.compare(b) <= 0;
//	}
//	else {
//		return a.size() < b.size();
//	}
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N;
//	cin >> N;
//
//	string* word = new string[N];
//
//	for (int i = 0; i < N; i++) {
//		cin >> word[i];
//	}
//
//	mergeSort(word, 0, N - 1, true, stringCmp);
//
//	cout << word[0] << '\n';
//	for (int i = 1; i < N; i++) {
//		if (word[i].compare(word[i-1])) {
//			cout << word[i] << '\n';
//		}
//	}
//
//	return 0;
//}