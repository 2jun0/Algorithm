//#include <iostream>
//#include<cstring>
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
//		sorted = new T[end - start + 1];
//
//		while (i <= mid && j <= end) {
//			if (cmp(arr[i], arr[j]) == isAscending) {
//				sorted[s++] = arr[i++];
//			}
//			else {
//				sorted[s++] = arr[j++];
//			}
//		}
//
//		while (i <= mid) { sorted[s++] = arr[i++]; }
//		while (j <= end) { sorted[s++] = arr[j++]; }
//
//		for (int k = 0; k <= end - start; k++) {
//			arr[k + start] = sorted[k];
//		}
//
//		delete[] sorted;
//	}
//}
//
//class Line {
//public:
//	int start, end;
//	Line() {}
//	Line(int start, int end):start(start), end(end) {}
//};
//
//bool cmpLine(Line& a, Line& b) { return a.start <= b.start; }
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int n;
//	cin >> n;
//
//	Line* lines = new Line[n];
//
//	for (int i = 0; i < n; i++) {
//		cin >> lines[i].start >> lines[i].end;
//	}
//	mergeSort(lines, 0, n - 1, true, cmpLine);
//
//	int len = lines[0].end - lines[0].start;
//	int idx = lines[0].end;
//	for (int i = 1; i < n; i++) {
//		if (lines[i].start <= idx) {
//			if (lines[i].end > idx) {
//				len += lines[i].end - idx;
//				idx = lines[i].end;
//			}
//		}
//		else {
//			len += (lines[i].end - lines[i].start);
//			idx = lines[i].end;
//		}
//	}
//	cout << len;
//
//	return 0;
//}