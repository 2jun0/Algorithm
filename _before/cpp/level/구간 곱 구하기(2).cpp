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
//#define MOD 1000000007
//
//template<typename T>
//class MulSegmentTree {
//	class Node {
//	public:
//		T value;
//		Node* left;
//		Node* right;
//		Node(T value) : value(value), left(NULL), right(NULL) { }
//		Node() : left(NULL), right(NULL) { }
//		~Node() { delete left; delete right; }
//	};
//private:
//	Node* root;
//	int n;
//	Node* init(const T* arr, int start, int end) {
//		if (start == end) {
//			return new Node(arr[start]);
//		}
//
//		Node* node = new Node();
//		int mid = (start + end) / 2;
//		node->left = init(arr, start, mid);
//		node->right = init(arr, mid + 1, end);
//
//		node->value = (node->left->value * node->right->value)%MOD;
//		return node;
//	}
//	T _mul(Node* node, int start, int end, int left, int right) {
//		if ((start > right || end < left) || start > end) {
//			return 1; // 찾을 수 없다.
//		}
//		else if (left <= start && end <= right) {
//			return node->value;
//		}
//		else {
//			int mid = (start + end) / 2;
//			return (_mul(node->left, start, mid, left, right) * _mul(node->right, mid + 1, end, left, right))%MOD;
//		}
//	}
//	T _update(Node* node, int start, int end, int index, T num) {
//		if ((index < start || index > end) || start > end) return node->value;
//		if (start == end) { // index
//			node->value = num;
//			return node->value;
//		}
//		else {
//			int mid = (start + end) / 2;
//
//			_update(node->left, start, mid, index, num);
//			_update(node->right, mid + 1, end, index, num);
//			node->value = (node->left->value * node->right->value)%MOD;
//			node->value %= MOD;
//			return node->value;
//		}
//	}
//public:
//	MulSegmentTree(const T* arr, int n) : n(n) {
//		root = init(arr, 0, n - 1);
//	}
//	~MulSegmentTree() {
//		delete root;
//	}
//	T mul(int left, int right) {
//		return _mul(root, 0, n - 1, left, right);
//	}
//	void update(int idx, T num) {
//		_update(root, 0, n - 1, idx, num);
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
//	for (int i = 0; i < n; i++) {
//		cin >> A[i];
//	}
//	MulSegmentTree<long long> tree(A, n);
//	delete[] A;
//
//	for (int _ = 0; _ < k+m; _++) {
//		int type, a1, a2;
//		cin >> type >> a1 >> a2;
//		if (type == 1) {
//			tree.update(a1-1, a2);
//		}
//		else {
//			cout << tree.mul(a1-1, a2-1) << '\n';
//		}
//	}
//
//
//	
//	return 0;
//}