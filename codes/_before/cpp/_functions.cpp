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

namespace test {
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
					sorted[s++] = arr[i++];
				}
				else {
					sorted[s++] = arr[j++];
				}
			}

			while (i <= mid) { sorted[s++] = arr[i++]; }
			while (j <= end) { sorted[s++] = arr[j++]; }

			for (int k = 0; k <= end - start; k++) {
				arr[k + start] = sorted[k];
			}

			delete[] sorted;
		}
	}
	template<typename T, typename U>
	void mergeSortWith(T* arr, U* arr2, int start, int end, bool isAscending = true, bool (*cmp)(T&, T&) = _defaultCmp) {
		int mid = (start + end) / 2;
		T* sorted; U* sorted2;
		int s = 0, i = start, j = mid + 1;

		if (start < end) {
			mergeSortWith(arr, arr2, start, mid, isAscending, cmp);
			mergeSortWith(arr, arr2, mid + 1, end, isAscending, cmp);
			sorted = new T[end - start + 1]; sorted2 = new U[end - start + 1];

			while (i <= mid && j <= end) {
				if (cmp(arr[i], arr[j]) == isAscending) {
					sorted[s] = arr[i]; sorted2[s++] = arr2[i++];
				}
				else {
					sorted[s] = arr[j]; sorted2[s++] = arr2[j++];
				}
			}

			while (i <= mid) { sorted[s] = arr[i]; sorted2[s++] = arr2[i++]; }
			while (j <= end) { sorted[s] = arr[j]; sorted2[s++] = arr2[j++]; }

			for (int k = 0; k <= end - start; k++) {
				arr[k + start] = sorted[k]; arr2[k + start] = sorted2[k];
			}

			delete[] sorted;
		}
	}

	int gcd(int a, int b) {
		int n, temp;
		if (a < b) {
			SWAP(a, b, temp);
		}

		while (b != 0) {
			n = a % b;
			a = b;
			b = n;
		}

		return a;
	}

	int _bino(int n, int r, int** memo) {
		if (r == 0 || n == r) {
			return 1;
		}
		else if (memo[n][r] != -1) {
			return memo[n][r];
		}
		else {
			return (memo[n][r] = _bino(n - 1, r, memo) + _bino(n - 1, r - 1, memo));
		}
	}

	int bino(int n, int r) {
		int** memo = new int* [n+1];
		for (int i = 0; i < n+1; i++) {
			memo[i] = new int[r+1];
			memset(memo[i], -1, sizeof(int) * (r+1));
		}

		int temp = _bino(n, r, memo);
		for (int i = 0; i < n; i++) delete[] memo[i];
		delete[] memo;
		return temp;
	}

	void factorize(int& target, vector<int>& factors, bool includeOne = true) {
		int i;
		if (includeOne) { i = 1; }
		else { i = 2; }

		for (; i * i <= target; i++) {
			if (target% i == 0) {
				factors.push_back(i);
				if (target / i != i) factors.push_back(target / i);
			}
		}
	}

	int pow(int n, int k) {
		if (k == 0) {
			return 1;
		}

		long long temp = pow(n, k / 2);
		long long temp2 = temp * temp;

		if (k % 2 == 0) {
			return temp2;
		}
		else {
			return temp2 * n;
		}
	}

	long long powMod(int n, int k, int mod) {
		if (k == 0) {
			return 1;
		}

		long long temp = powMod(n, k / 2, mod);
		long long temp2 = (temp * temp) % mod;

		if (k % 2 == 0) {
			return temp2;
		}
		else {
			return (temp2 * n) % mod;
		}
	}

	int getPisanoPeriod(int mod) {
		int f1 = 0;
		int f2 = 1;
		int temp;

		int p = 1;
		while (true) {
			temp = f2;
			f2 = (f1 + f2) % mod;
			f1 = temp;

			if (f1 == 0 && f2 == 1) {
				return p;
			}

			p++;
		}
	}

	class Fraction {
	public:
		long long up;
		long long down;
		Fraction(long long up, long long down) : up(up), down(down) {}
		Fraction(long long up) : up(up), down(1) {}
		Fraction(const Fraction& f) : up(f.up), down(f.down) {}
		Fraction operator* (Fraction f) { return Fraction(f.up * up, f.down * down); }
		Fraction operator/ (Fraction f) { return Fraction(up / f.up, down / f.down); }
		Fraction operator% (const int& mod) { return Fraction(up % mod, down % mod); }
	};
	inline long long operator* (const int& num, const Fraction& f) {
		if (num == f.down) {
			return f.up;
		}
		return  num * f.up / f.down;
	}
}