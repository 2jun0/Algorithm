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
//class MulSegmentTree {
//	class Node {
//	public:
//		long long value;
//		Node* left;
//		Node* right;
//		Node(long long value) : value(value), left(NULL), right(NULL) { }
//		Node() : Node(1) { }
//		~Node() { delete left; delete right; }
//	};
//private:
//	Node* root;
//	int n;
//	Node* init(int start, int end) {
//		Node* node = new Node();
//		if (start < end) {
//			int mid = (start + end) / 2;
//			node->left = init(start, mid);
//			node->right = init(mid + 1, end);
//		}
//		return node;
//	}
//
//	long long mul(Node* node, int start, int end, int left, int right) {
//		if ((start > right || end < left) || start > end) {
//			return 1; // 찾을 수 없다.
//		}
//		else if (left <= start && end <= right) {
//			return node->value;
//		}
//		else {
//			int mid = (start + end) / 2;
//			return mul(node->left, start, mid, left, right) * mul(node->right, mid + 1, end, left, right);
//		}
//	}
//	void update(Node* node, int start, int end, int idx, long long num) {
//		if(start <= idx && idx <= end) {
//			if (start == end) { // idx
//				node->value = num;
//				return;
//			}
//
//			int mid = (start + end) / 2;
//			update(node->left, start, mid, idx, num);
//			update(node->right, mid + 1, end, idx, num);
//			node->value = node->left->value * node->right->value;
//		}
//	}
//public:
//	MulSegmentTree(int n) : n(n) {
//		root = init(0, n - 1);
//	}
//	~MulSegmentTree() {
//		delete root;
//	}
//	long long mul(int left, int right) {
//		return mul(root, 0, n - 1, left, right);
//	}
//	void update(int idx, long long num) {
//		update(root, 0, n - 1, idx, num);
//	}
//};
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int n, k;
//	while(cin >> n >> k) {
//		MulSegmentTree tree(n + 1);
//
//		for (int i = 1; i <= n; i++) {
//			long long num;
//			cin >> num;
//			if (num != 0) num = (num > 0) ? 1 : -1;
//			tree.update(i, num);
//		}
//
//		for (int _ = 0; _ < k; _++) {
//			char cmd;
//			cin >> cmd;
//			if (cmd == 'C') {
//				int i, V;
//				cin >> i >> V;
//				if (V != 0) V = (V > 0) ? 1 : -1;
//				tree.update(i, V);
//			}
//			else {
//				int i, j;
//				cin >> i >> j;
//				long long temp = tree.mul(i, j);
//				if (temp == 0) cout << 0;
//				else if (temp < 0) cout << '-';
//				else cout << '+';
//			}
//		}
//		cout << '\n';
//	}
//
//	return 0;
//}