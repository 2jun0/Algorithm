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
//				value = (end - start + 1) * lazy;
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
//	void _update(Node* node, int start, int end, int left, int right, long long val) {
//		node->lazyPropagate(start, end);
//		if ((start > right || end < left) || start > end) {
//			// 찾을 수 없다.
//		}
//		else if (left <= start && end <= right) {
//			node->lazy = val;
//			node->lazyPropagate(start, end);
//		}
//		else {
//			int mid = (start + end) / 2;
//			_update(node->left, start, mid, left, right, val);
//			_update(node->right, mid + 1, end, left, right, val);
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
//	void update(int left, int right, long long val) {
//		_update(root, 0, n - 1, left, right, val);
//	}
//};
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int C, N, O;
//	cin >> C >> N >> O;
//	long long* arr = new long long[C];
//	for (int i = 0; i < C; i++) {
//		arr[i] = 0;
//	}
//	LazySumSegmentTree tree(arr, C);
//	delete[] arr;
//
//	for (int i = 0; i < O; i++) {
//		string cmd;
//		cin >> cmd;
//
//		if (cmd.compare("change")==0) {
//			long long X, S;
//			cin >> X >> S;
//			tree.update(X, X, S);
//		}
//		else if (cmd.compare("groupchange") == 0 ) {
//			long long A, B, S;
//			cin >> A >> B >> S;
//			tree.update(A, B, S);
//			cout << B - A + 1 << '\n';
//		}
//		else if (cmd.compare("state") == 0 ) {
//			long long X;
//			cin >> X;
//			cout << tree.sum(X, X) << "\n";
//		}
//	}
//	
//	return 0;
//}