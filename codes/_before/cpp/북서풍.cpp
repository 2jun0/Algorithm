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
//class Dot {
//public:
//	int x, y;
//	Dot() {}
//	Dot(int x, int y) :x(x), y(y) {}
//};
//
//class MinSegmentTree {
//	class Node {
//	public:
//		Dot& value;
//		Node* left;
//		Node* right;
//		Node(Dot& value) : value(value), left(NULL), right(NULL) { }
//		Node() : left(NULL), right(NULL) { }
//		~Node() { delete left; delete right; }
//	};
//private:
//	Node* root;
//	int n;
//	Node* init(Dot* arr, int start, int end) {
//		if (start == end) {
//			return new Node(arr[start]);
//		}
//
//		Node* node = new Node();
//		int mid = (start + end) / 2;
//		node->left = init(arr, start, mid);
//		node->right = init(arr, mid + 1, end);
//
//		if (node->left->value.y > node->right->value.y) {
//			node->value = node->right->value;
//		}
//		else {
//			node->value = node->left->value;
//		}
//		return node;
//	}
//	Dot* _min(Node* node, int start, int end, int left, int right) {
//		if ((start > right || end < left) || start > end) {
//			return NULL; // 찾을 수 없다.
//		}
//		else if (left <= start && end <= right) {
//			return &node->value;
//		}
//		else {
//			int mid = (start + end) / 2;
//			Dot* a1 = _min(node->left, start, mid, left, right);
//			Dot* a2 = _min(node->right, mid + 1, end, left, right);
//			if (a1 == NULL)
//				return a2;
//			else if (a2 == NULL)
//				return a1;
//			else
//				if (a1->y > a2->y) {
//					return a2;
//				}
//				else {
//					return a1;
//				}
//		}
//	}
//	Dot _update(Node* node, int start, int end, int index, Dot num) {
//		if ((index < start || index > end) || start > end) return node->value;
//		if (start == end) { // index
//			node->value = num;
//			return num;
//		}
//		else {
//			int mid = (start + end) / 2;
//			node->value = std::min(_update(node->left, start, mid, index, num), _update(node->right, mid + 1, end, index, num));
//			return node->value;
//		}
//	}
//public:
//	MinSegmentTree(const Dot* arr, int n) : n(n) {
//		root = init(arr, 0, n - 1);
//	}
//	~MinSegmentTree() {
//		delete root;
//	}
//	Dot min(int left, int right) {
//		return _min(root, 0, n - 1, left, right);
//	}
//	void update(int idx, Dot num) {
//		_update(root, 0, n - 1, idx, num);
//	}
//};
//
//template<typename T>
//bool _defaultCmp(T& a, T& b) { return a <= b; }
//template<typename T>
//void mergeSort(T* arr, int start, int end, bool isAscending = true, bool (*cmp)(T&, T&) = _defaultCmp) {
//	int mid = (start + end) / 2;
//	T* sorted;
//	int s = 0, i = start, j = mid + 1;
//
//	if (start < end) {
//		mergeSort(arr, start, mid, isAscending, cmp);
//		mergeSort(arr, mid + 1, end, isAscending, cmp);
//		sorted = new T[end - start + 1];
//
//		while (i <= mid && j <= end) {
//			if (cmp(arr[i], arr[j]) == isAscending) {
//				sorted[s++] = arr[i++];
//			}
//			else {
//				sorted[s++] = arr[j++];
//			}
//		}
//
//		while (i <= mid) { sorted[s++] = arr[i++]; }
//		while (j <= end) { sorted[s++] = arr[j++]; }
//
//		for (int k = 0; k <= end - start; k++) {
//			arr[k + start] = sorted[k];
//		}
//
//		delete[] sorted;
//	}
//}
//
//bool cmpDot(Dot& a, Dot& b) {
//	if (a.x == b.x) {
//		return a.y >= b.y;
//	}
//	else {
//		return a.x < b.x;
//	}
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int T;
//	cin >> T;
//
//	for (int t = 0; t < T; t++) {
//		int n;
//		cin >> n;
//
//		Dot* dots = new Dot[n];
//
//		for (int i = 0; i < n; i++) {
//			cin >> dots[i].x >> dots[i].y;
//		}
//		mergeSort(dots, 0, n - 1, true, cmpDot);
//
//		int cnt = 0;
//		Dot* currDot = &dots[0];
//		int matchCnt = 0;
//		for (int i = 1; i < n; i++) {
//			if(currDot->x )
//		}
//		
//		delete[] dots;
//	}
//
//	return 0;
//}
//// -1 2
//// 0 5
//// 1 4
//// -1 0
//// -1 0