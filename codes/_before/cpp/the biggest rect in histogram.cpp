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
//class SegmentTree {
//	class Node {
//	public:
//		int idx;
//		Node* left;
//		Node* right;
//		Node(int idx): idx(idx), left(NULL), right(NULL) { }
//		Node() : left(NULL), right(NULL) { }
//		~Node() { delete left; delete right; }
//	};
//private:
//	Node* root;
//	int* arr;
//	int n;
//	Node* init(const int* arr, int start, int end) {
//		if (start == end) {
//			return new Node(start);
//		}
//
//		Node* node = new Node();
//		int mid = (start + end) / 2;
//		node->left = init(arr, start, mid);
//		node->right = init(arr, mid + 1, end);
//
//		if (arr[node->left->idx] < arr[node->right->idx]) {
//			node->idx = node->left->idx;
//		}
//		else {
//			node->idx = node->right->idx;
//		}
//		return node;
//	}
//	int _min(Node* node, int start, int end, int left, int right) {
//		if (start > right || end < left) {
//			return -1; // 찾을 수 없다.
//		}
//		else if (left <= start && end <= right) {
//			return node->idx;
//		} 
//		else {
//			int mid = (start + end) / 2;
//			int leftIdx = _min(node->left, start, mid, left, right);
//			int rightIdx = _min(node->right, mid + 1, end, left, right);
//
//			if (rightIdx == -1 || (leftIdx != -1 && arr[leftIdx] < arr[rightIdx]))
//				return leftIdx;
//			else
//				return rightIdx;
//		}
//	}
//public:
//	SegmentTree(int* arr, int n): arr(arr), n(n) {
//		root = init(arr, 0, n-1);
//	}
//	~SegmentTree() {
//		delete root;
//	}
//	int min(int left, int right) {
//		return _min(root, 0, n-1, left, right);
//	}
//};
//
//long long getBiggestRect(SegmentTree& tree, int *arr, int start, int end) {
//	if (start >= end) {
//		return arr[start];
//	}
//	
//	int minIdx = tree.min(start, end);
//	   
//	long long a1 = arr[minIdx] * ((long long)end - start + 1);
//	long long a2 = (minIdx > start) ? getBiggestRect(tree, arr, start, minIdx-1) : 0;
//	long long a3 = (minIdx < end) ? getBiggestRect(tree, arr, minIdx+1, end) : 0;
//	return max(max(a1, a2), a3);
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int n;
//	cin >> n;
//	while (n > 0) {
//		int* h = new int[n];
//		for (int i = 0; i < n; i++) {
//			cin >> h[i];
//		}
//
//		SegmentTree tree(h, n);
//		cout << getBiggestRect(tree, h, 0, n - 1) << '\n';
//
//		delete[] h;
//		cin >> n;
//	}
//	return 0;
//}