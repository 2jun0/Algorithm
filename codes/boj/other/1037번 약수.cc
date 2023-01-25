#include <iostream>
#include<cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <stack>
#include <vector>
#include <set>

#define ABS(x) (((x) < 0)?-(x):(x))
#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
#define PI 3.1415926535897932384

using namespace std;

template<typename T>
bool _defaultCmp(T& a, T& b) { return a <= b; }
template<typename T>
void mergeSort(T* arr, int start, int end, bool isAscending = true, bool (*cmp)(T&, T&) = _defaultCmp) {
	int mid = (start + end) / 2;
	T* sorted;
	int s = 0, i = start, j = mid + 1;

	if (start < end) {
		mergeSort(arr, start, mid, isAscending, cmp);
		mergeSort(arr, mid + 1, end, isAscending, cmp);

		sorted = new T[end - start + 1];

		while (i <= mid && j <= end) {
			if (cmp(arr[i], arr[j]) == isAscending) {
				sorted[s] = arr[i];
				i++;
			}
			else {
				sorted[s] = arr[j];
				j++;
			}
			s++;
		}

		while (i <= mid) {
			sorted[s] = arr[i];
			i++;  s++;
		}

		while (j <= end) {
			sorted[s] = arr[j];
			j++;  s++;
		}

		for (int k = 0; k <= end - start; k++) {
			arr[k + start] = sorted[k];
		}

		delete[] sorted;
	}
}

int main() {
	ios_base::sync_with_stdio(false);

	int factor_cnt;
	cin >> factor_cnt;

	int* factors = new int[factor_cnt];

	for (int i = 0; i < factor_cnt; i++) {
		cin >> factors[i];
	}
	mergeSort(factors, 0, factor_cnt - 1);

	cout << factors[0] * factors[factor_cnt-1];

	return 0;
}