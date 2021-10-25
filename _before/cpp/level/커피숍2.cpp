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
//class FenwickTree {
//private:
//	vector<T> data;
//public:
//	FenwickTree(const T* arr, int n) : data(n + 1) {
//		for (int i = 1; i <= n; i++) {
//			update(i, arr[i - 1]);
//		}
//	}
//	FenwickTree(int n) : data(n + 1) { }
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
//		return sum(right) - sum(left-1);
//	}
//	void update(int i, T diff) {
//		while (i < data.size()) {
//			data[i] += diff;
//			i += (i & -i); // 최하위 비트 더하면 상위로 올라감
//		}
//	}
//};
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int n, q;
//	cin >> n >> q;
//
//	long long* A = new long long[n];
//
//	for (int i = 0; i < n; i++) {
//		cin >> A[i];
//	}
//	FenwickTree<long long> tree(A,n);
//
//	for (int _ = 0; _ < q; _++) {
//		int start, end, idx, num;
//		cin >> start >> end;
//		if (start > end) swap(start, end);
//		cout << tree.sum(start, end) << '\n';
//
//		cin >> idx >> num;
//		long long diff = num - A[idx-1];
//		A[idx-1] = num;
//		tree.update(idx, diff);
//	}
//
//
//	delete[] A;
//	return 0;
//}