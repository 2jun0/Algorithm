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
//		i += 1;
//		long long ans = 0;
//		while (i > 0) {
//			ans += data[i];
//			i -= (i & -i); //최하위 비트 지우기
//		}
//		return ans;
//	}
//	void update(int i, T diff) {
//		i += 1;
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
//	int n;
//	cin >> n;
//
//	int* A = new int[n];
//	map<int, int> Bidxes;
//
//	for (int i = 0; i < n; i++) {
//		cin >> A[i];
//	}
//
//	int B;
//	for (int i = 0; i < n; i++) {
//		cin >> B;
//		Bidxes[B] = i;
//	}
//
//	FenwickTree<int> tree(n);
//
//	long long ans = 0;
//	for (int i = 0; i < n; i++) {
//		int valA = A[i];
//		int idxB = Bidxes[valA];
//		
//		ans += tree.sum(n-1) - tree.sum(idxB);
//		tree.update(idxB, 1);
//	}
//
//	cout << ans;
//
//	delete[] A;
//	return 0;
//}