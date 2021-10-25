#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;

using namespace std;

template<typename T>
bool _defaultCmp(T& a, T& b) { return a <= b; }
template<typename T>
void mergeSort(T* arr, int start, int end, bool isAscending = true, bool (*cmp)(T&, T&) = _defaultCmp) {
	int mid = (start + end) / 2;
	T* sorted;
	int s = 0;
	int i = start, j = mid + 1;

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

template<typename T>
void mergeSort(T* arr, int start, int end, bool isAscending = true) {
	int mid = (start + end) / 2;
	T* sorted;
	int s = 0;
	int i = start, j = mid + 1;

	if (start < end) {
		mergeSort(arr, start, mid, isAscending);
		mergeSort(arr, mid + 1, end, isAscending);

		sorted = new T[end - start + 1];

		while (i <= mid && j <= end) {
			if (isAscending) {
				if (arr[i] <= arr[j]) {
					sorted[s] = arr[i];
					i++;
				}
				else {
					sorted[s] = arr[j];
					j++;
				}
				s++;
			}
			else {
				if (arr[i] >= arr[j]) {
					sorted[s] = arr[i];
					i++;
				}
				else {
					sorted[s] = arr[j];
					j++;
				}
				s++;
			}
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

template <typename T>
void quickSort(T* arr, int start, int end, bool isAscending = true) {

	int pivot = start;
	int temp;
	int i = start + 1, j = start;

	if (start < end) {
		if (isAscending) {
			while (i <= end) {
				if (arr[i] < arr[pivot]) {
					j++;
					SWAP(arr[i], arr[j], temp);
				}
				i++;
			}
		}
		else {
			while (i <= end) {
				if (arr[i] > arr[pivot]) {
					j++;
					SWAP(arr[i], arr[j], temp);
				}
				i++;
			}
		}

		SWAP(arr[j], arr[pivot], temp);

		quickSort(arr, start, j - 1, isAscending);
		quickSort(arr, j + 1, end, isAscending);
	}
}