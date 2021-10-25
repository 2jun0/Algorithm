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
//class LazySumSegmentTree {
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
//					left->lazy += lazy;
//					right->lazy += lazy;	
//				}
//				value += (end - start + 1) * lazy;
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
//		node->value = node->left->value + node->right->value;
//		return node;
//	}
//	long long _sum(Node* node, int start, int end, int left, int right) {
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
//				return _sum(node->left, start, mid, left, right) + _sum(node->right, mid + 1, end, left, right);
//			}
//		}
//	}
//	void _update(Node* node, int start, int end, int left, int right, long long diff) {
//		node->lazyPropagate(start, end);
//		if ((start > right || end < left) || start > end) {
//			// 찾을 수 없다.
//		}
//		else if (left <= start && end <= right) {
//			node->lazy += diff;
//			node->lazyPropagate(start, end);
//		}
//		else {
//			int mid = (start + end) / 2;
//			_update(node->left, start, mid, left, right, diff);
//			_update(node->right, mid + 1, end, left, right, diff);
//			node->value = node->left->value + node->right->value;
//		}
//	}
//public:
//	LazySumSegmentTree(const long long* arr, int n) : n(n) {
//		root = init(arr, 0, n - 1);
//	}
//	~LazySumSegmentTree() {
//		delete root;
//	}
//	long long sum(int left, int right) {
//		return _sum(root, 0, n - 1, left, right);
//	}
//	void update(int left, int right, long long diff) {
//		_update(root, 0, n - 1, left, right, diff);
//	}
//};
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int n, m, k;
//	cin >> n >> m >> k;
//	long long* arr = new long long[n];
//	for (int i = 0; i < n; i++) {
//		cin >> arr[i];
//	}
//	LazySumSegmentTree switches(arr, n);
//	delete[] arr;
//
//	for (int i = 0; i < m+k; i++) {
//		long long a, b, c, d;
//		cin >> a;
//
//		if (a == 1) {
//			cin >> b >> c >> d;
//			switches.update(b-1,c-1,d);
//		}
//		else {
//			cin >> b >> c;
//			cout << switches.sum(b-1,c-1) << '\n';
//		}
//	}
//
//	return 0;
//}