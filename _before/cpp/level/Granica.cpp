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
//int gcd(int a, int b) {
//	int n, temp;
//	if (a < b) {
//		SWAP(a, b, temp);
//	}
//
//	while (b != 0) {
//		n = a % b;
//		a = b;
//		b = n;
//	}
//
//	return a;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N;
//	cin >> N;
//
//	int* nums = new int[N];
//	for (int i = 0; i < N; i++) {
//		cin >> nums[i];
//	}
//
//	mergeSort(nums, 0, N - 1);
//
//	int diff = nums[1] - nums[0];
//	for (int i = 1; i < N - 1; i++) {
//		diff = gcd(diff, nums[i + 1] - nums[i]);
//	}
//
//	vector<int> factors;
//	for (int i = 2; i*i <= diff; i++) {
//		if (diff % i == 0) {
//			factors.push_back(i);
//			if (diff / i != i) factors.push_back(diff / i);
//		}
//	}
//	factors.push_back(diff);
//
//	sort(factors.begin(), factors.end());
//
//	for (int& factor : factors) {
//		cout << factor << " ";
//	}
//
//	return 0;
//}