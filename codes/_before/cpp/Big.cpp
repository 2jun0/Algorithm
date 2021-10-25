//#include <iostream>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//
//#define MIN(x,y) ((x > y)?(y):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//#include <set>
//template<typename T>
//class XorSet: public set<T>{
//public:
//	XorSet() : set<T>() {
//
//	}
//
// 	void insert(T item) {
//		typename std::set<T>::iterator iter;
//		iter = set<T>::find(item);
//
//		if(iter != set<T>::end()) {
//			set<T>::erase(iter);
//		}
//		else {
//			set<T>::insert(item);
//		}
//	}
//};
//
//template<typename T>
//void swapArray(T* arr, int n) {
//	T temp;
//	for (int i = 0; i < n/2; i++) {
//		temp = arr[i];
//		arr[i] = arr[n - 1 - i];
//		arr[n - 1 - i] = temp;
//	}
//}
//
//void quick_sort(int* data, int start, int end, int* sortedIdx) {
//	if (start >= end) { // 원소가 1개인 경우
//		return; 
//	}
//		
//	int pivot = start;
//	int i = pivot + 1; // 왼쪽 출발 지점
//	int j = end; // 오른쪽 출발 지점
//	int temp; while(i <= j){ 
//		// 포인터가 엇갈릴때까지 반복
//		while(i <= end && data[i] >= data[pivot]){ i++; } 
//		while(j > start && data[j] <= data[pivot]){ j--; }
//		if(i > j){ // 엇갈림
//			temp = sortedIdx[j];
//			sortedIdx[j] = sortedIdx[pivot];
//			sortedIdx[pivot] = temp;
//			temp = data[j];
//			data[j] = data[pivot];
//			data[pivot] = temp;
//		}else{ 
//			// i번째와 j번째를 스왑 
//			temp = sortedIdx[i];
//			sortedIdx[i] = sortedIdx[j]; 
//			sortedIdx[j] = temp; 
//			temp = data[i];
//			data[i] = data[j];
//			data[j] = temp;
//		}
//
//	} // 분할 계산 
//	quick_sort(data, start, j - 1, sortedIdx);
//	quick_sort(data, j + 1, end, sortedIdx);
//}
//
//int main() {
//	int N;
//
//	cin >> N;
//
//	int* bigs_weight = new int[N];
//	int* sortedIdx_weight = new int[N];
//	int* bigs_tall = new int[N];
//	int* sortedIdx_tall = new int[N];
//
//	for (int i = 0; i < N; i++) {
//		cin >> bigs_weight[i];
//		cin >> bigs_tall[i];
//
//		sortedIdx_weight[i] = i;
//		sortedIdx_tall[i] = i;
//	}
//
//	quick_sort(bigs_weight, 0, N-1, sortedIdx_weight);
//	quick_sort(bigs_tall, 0, N - 1, sortedIdx_tall);
//
//	free(bigs_weight);
//	free(bigs_tall);
//
//	int* totalRank = new int[N];
//	int rank = 1;
//	int rank_temp = 0;
//	XorSet<int> xorSet;
//
//	for (int i = 0; i < N; i++) {
//		if (sortedIdx_weight[i] == sortedIdx_tall[i]) {
//			totalRank[sortedIdx_weight[i]] = rank;
//		}
//		else {
//			do {
//				xorSet.insert(sortedIdx_weight[i]);
//				xorSet.insert(sortedIdx_tall[i]);
//
//				totalRank[sortedIdx_weight[i]] = rank;
//				i++;
//				rank_temp++;
//			} while (!xorSet.empty());
//			i--;
//			rank += rank_temp - 1;
//			rank_temp = 0;
//		}
//
//		rank ++;
//	}
//
//	for (int i = 0; i < N; i++) {
//		cout << totalRank[i] << ' ';
//	}
//
//	return 0;
//}

//#include <iostream>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//
//#define MIN(x,y) ((x > y)?(y):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//int main() {
//	int N;
//
//	cin >> N;
//
//	int* bigs_weight = new int[N];
//	int* bigs_tall = new int[N];
//	int rank;
//
//	for (int i = 0; i < N; i++) {
//		cin >> bigs_weight[i];
//		cin >> bigs_tall[i];
//	}
//
//	for (int i = 0; i < N; i++) {
//		rank = 1;
//		for (int j = 0; j < N; j++) {
//			if (i == j) continue;
//
//			if (bigs_tall[i] < bigs_tall[j]) {
//				if (bigs_weight[i] < bigs_weight[j]) {
//					rank++;
//				}
//			}
//		}
//		cout << rank << ' ';
//	}
//
//	return 0;
//}