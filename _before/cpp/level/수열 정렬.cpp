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
//class Record {
//public:
//	int idx;
//	int val;
//	Record** link;
//	Record() { Record(0, 0, NULL); }
//	Record(int idx, int val, Record** link): idx(idx), val(val), link(link) {
//		if(link) *link = this;
//	}
//	Record operator= (const Record& record) {
//		idx = record.idx; val = record.val; link = record.link;
//		if (link) *link = this;
//		return *this;
//	}
//};
//bool recordCmp(Record& a, Record& b) { return a.val <= b.val; }
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int N;
//	cin >> N;
//
//	Record* records = new Record[N];
//	Record** searchor = new Record*[N];
//	for (int i = 0; i < N; i++)	{
//		searchor[i] = &records[i];
//		records[i].idx = i;
//		records[i].link = &searchor[i];
//		cin >> records[i].val;
//	}
//
//	mergeSort(records, 0, N - 1, true, recordCmp);
//
//	for (int i = 0; i < N; i++) {
//		records[i].idx = i;
//	}
//
//	for (int i = 0; i < N; i++) {
//		cout << searchor[i]->idx << ' ';
//	}
//
//	delete[] records, searchor;
//	return 0;
//}