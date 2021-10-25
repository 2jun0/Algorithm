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
//		return sum(right) - sum(left - 1);
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
//	int T;
//	cin >> T;
//	for (int t = 0; t < T; t++)	{
//		int n, m;
//		cin >> n >> m;
//
//		FenwickTree<long long> books(n+m);
//		int* bookIdxes = new int[n+1];
//		for (int i = 1; i <= n; i++) {
//			books.update(i, 1);
//			bookIdxes[i] = n-i+1;
//		}
//
//		for (int i = n+1; i <= m+n; i++) {
//			int book;
//			cin >> book;
//			cout << n-books.sum(bookIdxes[book]) << ' ';
//			books.update(bookIdxes[book], -1);
//			bookIdxes[book] = i;
//			books.update(bookIdxes[book], 1);
//		}
//		cout << '\n';
//
//		delete[] bookIdxes;
//	}
//
//	return 0;
//}