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
//		int value;
//		Node* left;
//		Node* right;
//		bool lazy;
//		Node(int value) : value(value), left(NULL), right(NULL), lazy(0) { }
//		Node() : left(NULL), right(NULL), lazy(0) { }
//		~Node() { delete left; delete right; }
//		void lazyPropagate(int start, int end) {
//			if (lazy) {
//				if (left != NULL) {
//					left->lazy = !left->lazy;
//					right->lazy = !right->lazy;
//				}
//				value = end - start + 1 - value;
//				lazy = false;
//			}
//		}
//	};
//private:
//	Node* root;
//	int n;
//	Node* init(const int* arr, int start, int end) {
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
//	int _sum(Node* node, int start, int end, int left, int right) {
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
//	void _reverse(Node* node, int start, int end, int left, int right) {
//		node->lazyPropagate(start, end);
//		if ((start > right || end < left) || start > end) {
//			// 찾을 수 없다.
//		}
//		else if (left <= start&& end <= right) {
//				node->lazy = !node->lazy;
//				node->lazyPropagate(start, end);
//		}
//		else {
//			int mid = (start + end) / 2;
//			_reverse(node->left, start, mid, left, right);
//			_reverse(node->right, mid + 1, end, left, right);
//			node->value = node->left->value + node->right->value;
//		}
//	}
//public:
//	LazySumSegmentTree(const int* arr, int n) : n(n) {
//		root = init(arr, 0, n - 1);
//	}
//	~LazySumSegmentTree() {
//		delete root;
//	}
//	int sum(int left, int right) {
//		return _sum(root, 0, n - 1, left, right);
//	}
//	void reverse(int left, int right) {
//		_reverse(root, 0, n - 1, left, right);
//	}
//};
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int n, m;
//	cin >> n >> m;
//	int* arr = new int[n];
//	memset(arr, 0, sizeof(int) * n);
//	LazySumSegmentTree switches(arr, n);
//
//	for (int i = 0; i < m; i++) {
//		int O, S, T;
//		cin >> O >> S >> T;
//
//		if (O == 0) {
//			switches.reverse(S-1, T-1);
//		}
//		else {
//			cout << switches.sum(S - 1, T - 1) << '\n';
//		}
//	}
//
//	delete[] arr;
//
//	return 0;
//}