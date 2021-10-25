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
//class SumSegmentTree {
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
//		node->value = node->left->value + node->right->value;
//		return node;
//	}
//	T _sum(Node* node, int start, int end, int left, int right) {
//		if ((start > right || end < left) || start > end) {
//			return 0; // 찾을 수 없다.
//		}
//		else if (left <= start && end <= right) {
//			return node->value;
//		}
//		else {
//			int mid = (start + end) / 2;
//			return _sum(node->left, start, mid, left, right) + _sum(node->right, mid + 1, end, left, right);
//		}
//	}
//	T _update(Node* node, int start, int end, int index, T num) {
//		if ((index < start || index > end) || start > end) return 0;
//		if (start == end) { // index
//			T diff = num - node->value;
//			node->value = num;
//			return diff;
//		}
//		else {
//			int mid = (start + end) / 2;
//			T diff = _update(node->left, start, mid, index, num) + _update(node->right, mid + 1, end, index, num);
//			node->value += diff;
//			return diff;
//		}
//	}
//	int _search(Node* node, int start, int end, int rank) {
//		if (start == end) { // leaf node
//			return start;
//		}
//		else {
//			int mid = (start + end) / 2;
//			if (node->left->value >= rank) {
//				return _search(node->left, start, mid, rank);
//			}
//			else {
//				return _search(node->right, mid+1, end, rank - node->left->value);
//			}
//		}
//	}
//public:
//	SumSegmentTree(const T* arr, int n) : n(n) {
//		root = init(arr, 0, n - 1);
//	}
//	~SumSegmentTree() {
//		delete root;
//	}
//	T sum(int left, int right) {
//		return _sum(root, 0, n - 1, left, right);
//	}
//	void update(int idx, T num) {
//		_update(root, 0, n - 1, idx, num);
//	}
//	int search(int rank) {
//		return _search(root, 0, n - 1, rank);
//	}
//};
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int n;
//	cin >> n;
//	int* arr = new int[1000000];
//	memset(arr, 0, sizeof(int) * 1000000);
//	SumSegmentTree<int> candies(arr, 1000000);
//
//	for (int i = 0; i < n; i++) {
//		int A;
//		cin >> A;
//
//		if (A == 1) {
//			int rank;
//			cin >> rank;
//			int candy = candies.search(rank);
//			cout << candy +1 << '\n';
//			arr[candy] --;
//			candies.update(candy, arr[candy]);
//		}
//		else {
//			int candy, cnt;
//			cin >> candy >> cnt;
//			candy--;
//			arr[candy] += cnt;
//			candies.update(candy, arr[candy]);
//		}
//	}
//
//	delete[] arr;
//
//	return 0;
//}