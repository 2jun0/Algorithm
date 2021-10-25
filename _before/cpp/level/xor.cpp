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
//class LazyXorSegmentTree {
//	class Node {
//	public:
//		long long value;
//		Node* left;
//		Node* right;
//		long long lazy;
//		Node(long long value) : value(value), left(NULL), right(NULL), lazy(0) { }
//		Node() : left(NULL), right(NULL), lazy(0) { }
//		~Node() { delete left; delete right; }
//		void lazyPropagate(int start, int end) {
//			if (lazy != 0) {
//				if (left != NULL) {
//					left->lazy ^= lazy;
//					right->lazy ^= lazy;
//				}
//				if ((end - start+1)%2 == 1) {
//					value ^= lazy;
//				}
//
//				lazy = 0;
//			}
//		}
//	};
//private:
//	Node* root;
//	int n;
//	Node* init(const long long* arr, int start, int end) {
//		if (start == end) {
//			return new Node(arr[start]);
//		}
//
//		Node* node = new Node();
//		int mid = (start + end) / 2;
//		node->left = init(arr, start, mid);
//		node->right = init(arr, mid + 1, end);
//
//		node->value = node->left->value ^ node->right->value;
//		return node;
//	}
//	long long _XorSum(Node* node, int start, int end, int left, int right) {
//		node->lazyPropagate(start, end);
//		if ((start > right || end < left) || start > end) {
//			return 0; // 찾을 수 없다.
//		}
//		else {
//			if (left <= start && end <= right) {
//				return node->value;
//			}
//			else {
//				int mid = (start + end) / 2;
//				return _XorSum(node->left, start, mid, left, right) ^ _XorSum(node->right, mid + 1, end, left, right);
//			}
//		}
//	}
//	void _Xor(Node* node, int start, int end, int left, int right, long long diff) {
//		node->lazyPropagate(start, end);
//		if ((start > right || end < left) || start > end) {
//			// 찾을 수 없다.
//		}
//		else if (left <= start && end <= right) {
//			node->lazy ^= diff;
//			node->lazyPropagate(start, end);
//		}
//		else {
//			int mid = (start + end) / 2;
//			_Xor(node->left, start, mid, left, right, diff);
//			_Xor(node->right, mid + 1, end, left, right, diff);
//			node->value = node->left->value ^ node->right->value;
//		}
//	}
//public:
//	LazyXorSegmentTree(const long long* arr, int n) : n(n) {
//		root = init(arr, 0, n - 1);
//	}
//	~LazyXorSegmentTree() {
//		delete root;
//	}
//	long long XorSum(int left, int right) {
//		return _XorSum(root, 0, n - 1, left, right);
//	}
//	void Xor(int left, int right, long long diff) {
//		_Xor(root, 0, n - 1, left, right, diff);
//	}
//};
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int n;
//	cin >> n;
//	long long* arr = new long long[n];
//	for (int i = 0; i < n; i++) {
//		cin >> arr[i];
//	}
//	LazyXorSegmentTree xorTree(arr, n);
//	delete[] arr;
//
//	int m;
//	cin >> m;
//	for (int i = 0; i < m; i++) {
//		long long t, a, b, c;
//		cin >> t;
//		cin >> a >> b;
//
//		if (a > b) {
//			swap(a, b);
//		}
//
//		if (t == 1) {
//			cin >> c;
//			xorTree.Xor(a, b, c);
//		}
//		else {
//			cout << xorTree.XorSum(a, b) << '\n';
//		}
//	}
//
//	return 0;
//}