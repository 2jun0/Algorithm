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
//long long powMod(int n, int k, int mod) {
//	if (k == 0) {
//		return 1;
//	}
//
//	long long temp = powMod(n, k / 2, mod);
//	long long temp2 = (temp * temp) % mod;
//
//	if (k % 2 == 0) {
//		return temp2;
//	}
//	else {
//		return (temp2 * n) % mod;
//	}
//}
//
//template<typename T>
//class SumFenwickTree {
//private:
//	vector<T> data;
//public:
//	SumFenwickTree(const T* arr, int n) : data(n + 1) {
//		for (int i = 1; i <= n; i++) {
//			update(i, arr[i - 1]);
//		}
//	}
//	SumFenwickTree(int n) : data(n + 1) { }
//
//	long long sum(int i) {
//		long long ans = 0;
//		while (i > 0) {
//			ans += data[i];
//			i -= (i & -i); //최하위 비트 지우기
//		}
//		return ans;
//	}
//	long long sum(int left, int right) {
//		return sum(right) - sum(left - 1);
//	}
//	void update(int i, T diff) {
//		while (i < data.size()) {
//			data[i] += diff;
//			if (data[i] < 0) data[i] = 0;
//			i += (i & -i); // 최하위 비트 더하면 상위로 올라감
//		}
//	}
//};
//
//template<typename T>
//class MulFenwickTree {
//private:
//	vector<T> data;
//public:
//	MulFenwickTree(const T* arr, int n) : data(n + 1, 1) {
//		for (int i = 1; i <= n; i++) {
//			update(i, 1, arr[i - 1]);
//		}
//	}
//	MulFenwickTree(int n) : data(n + 1, 1) { }
//
//	long long mul(int i) {
//		long long ans = 1;
//		while (i > 0) {
//			ans *= data[i];
//			ans %= 1000000007;
//			i -= (i & -i); //최하위 비트 지우기
//		}
//		return ans;
//	}
//	long long mul(int left, int right) {
//		long long modInverse = powMod(mul(left - 1), 1000000005LL, 1000000007LL);
//		return (mul(right) * modInverse) % 1000000007LL;
//	}
//	void update(int i, T valOrigin, T valNew) {
//		// B가 하위 노드이고 A가 상위 노드(B포함)일때, B를 업데이트 할시, 다음을 만족
//		// A' : 새로운 A, B' : 새로운 B, m는 1000000007LL
//		// A' = (B*B'*(B^(m-2)%m))%m
//
//		long long modInverse = powMod(valOrigin, 1000000005LL, 1000000007LL);
//
//		while (i < data.size()) {
//			data[i] = ((data[i] * valNew) % 1000000007LL * modInverse) % 1000000007LL;
//			i += (i & -i); // 최하위 비트 더하면 상위로 올라감
//		}
//	}
//};
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int n, m, k;
//	cin >> n >> m >> k;
//
//	long long* A = new long long[n];
//
//	SumFenwickTree<int> zeroTree(n);
//	for (int i = 0; i < n; i++) {
//		cin >> A[i];
//		if (A[i] == 0) {
//			A[i] = 1;
//			zeroTree.update(i + 1, 1);
//		}
//	}
//	MulFenwickTree<long long> tree(A, n);
//
//	for (int _ = 0; _ < k+m; _++) {
//		int type, a1, a2;
//		cin >> type >> a1 >> a2;
//		if (type == 1) {
//			if (a2 == 0) {
//				if (zeroTree.sum(a1,a1) == 0) {
//					zeroTree.update(a1, 1);
//				}
//			}
//			else {
//				zeroTree.update(a1, -1);
//				tree.update(a1, A[a1 - 1], a2);
//				A[a1 - 1] = a2;
//			}
//		}
//		else {
//			if (zeroTree.sum(a1, a2) > 0) {
//				cout << 0 << '\n';
//			}
//			else {
//				cout << tree.mul(a1, a2) << '\n';
//			}
//		}
//	}
//
//
//	delete[] A;
//	return 0;
//}