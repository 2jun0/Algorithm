#include <iostream>
#include<cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <stack>
#include <vector>
#include <set>
#include <queue>
#include <map>

#define ABS(x) (((x) < 0)?-(x):(x))
#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
#define PI 3.1415926535897932384

using namespace std;

template<typename T>
class MinSegmentTree {
	class Node {
	public:
		T value;
		Node* left;
		Node* right;
		Node(T value) : value(value), left(NULL), right(NULL) { }
		Node() : left(NULL), right(NULL) { }
		~Node() { delete left; delete right; }
	};
private:
	Node* root;
	int n;
	Node* init(const T* arr, int start, int end) {
		if (start == end) {
			return new Node(arr[start]);
		}

		Node* node = new Node();
		int mid = (start + end) / 2;
		node->left = init(arr, start, mid);
		node->right = init(arr, mid + 1, end);

		node->value = std::min(node->left->value, node->right->value);
		return node;
	}
	T _min(Node* node, int start, int end, int left, int right) {
		if ((start > right || end < left) || start > end) {
			return -1; // 찾을 수 없다.
		}
		else if (left <= start && end <= right) {
			return node->value;
		}
		else {
			int mid = (start + end) / 2;
			int a2 = _min(node->left, start, mid, left, right);
			int a1 = _min(node->right, mid + 1, end, left, right);
			if (a1 == -1)
				return a2;
			else if (a2 == -1)
				return a1;
			else
				return std::min(a1, a2);
		}
	}
	T _update(Node* node, int start, int end, int index, T num) {
		if ((index < start || index > end) || start > end) return node->value;
		if (start == end) { // index
			node->value = num;
			return num;
		}
		else {
			int mid = (start + end) / 2;
			node->value = std::min(_update(node->left, start, mid, index, num), _update(node->right, mid + 1, end, index, num));
			return node->value;
		}
	}
public:
	MinSegmentTree(const T* arr, int n) : n(n) {
		root = init(arr, 0, n - 1);
	}
	~MinSegmentTree() {
		delete root;
	}
	T min(int left, int right) {
		return _min(root, 0, n - 1, left, right);
	}
	void update(int idx, T num) {
		_update(root, 0, n - 1, idx, num);
	}
};

template<typename T>
class MaxSegmentTree {
	class Node {
	public:
		T value;
		Node* left;
		Node* right;
		Node(T value) : value(value), left(NULL), right(NULL) { }
		Node() : left(NULL), right(NULL) { }
		~Node() { delete left; delete right; }
	};
private:
	Node* root;
	int n;
	Node* init(const T* arr, int start, int end) {
		if (start == end) {
			return new Node(arr[start]);
		}

		Node* node = new Node();
		int mid = (start + end) / 2;
		node->left = init(arr, start, mid);
		node->right = init(arr, mid + 1, end);

		node->value = std::max(node->left->value, node->right->value);
		return node;
	}
	T _max(Node* node, int start, int end, int left, int right) {
		if ((start > right || end < left) || start > end) {
			return -1; // 찾을 수 없다.
		}
		else if (left <= start && end <= right) {
			return node->value;
		}
		else {
			int mid = (start + end) / 2;
			int a2 = _max(node->left, start, mid, left, right);
			int a1 = _max(node->right, mid + 1, end, left, right);
			return std::max(a1, a2);
		}
	}
	T _update(Node* node, int start, int end, int index, T num) {
		if ((index < start || index > end) || start > end) return node->value;
		if (start == end) { // index
			node->value = num;
			return num;
		}
		else {
			int mid = (start + end) / 2;
			node->value = std::max(_update(node->left, start, mid, index, num), _update(node->right, mid + 1, end, index, num));
			return node->value;
		}
	}
public:
	MaxSegmentTree(const T* arr, int n) : n(n) {
		root = init(arr, 0, n - 1);
	}
	~MaxSegmentTree() {
		delete root;
	}
	T max(int left, int right) {
		return _max(root, 0, n - 1, left, right);
	}
	void update(int idx, T num) {
		_update(root, 0, n - 1, idx, num);
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int n, m;
	cin >> n >> m;

	int* arr = new int[n];

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	MinSegmentTree<int> minTree(arr, n);
	MaxSegmentTree<int> maxTree(arr, n);

	int left, right;
	for (int i = 0; i < m; i++) {
		cin >> left >> right;
		cout << minTree.min(left - 1, right - 1) << ' ' << maxTree.max(left - 1, right - 1) << '\n';
	}

	delete[] arr;
	return 0;
}