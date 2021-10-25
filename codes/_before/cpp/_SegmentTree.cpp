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

namespace seqmentTree {
	class SegmentTree {
		class Node {
		public:
			int value;
			Node* left;
			Node* right;
			Node(int value) : value(value), left(NULL), right(NULL) { }
			Node() : left(NULL), right(NULL) { }
			~Node() { delete left; delete right; }
		};
	private:
		Node* root;
		int n;
		Node* init(const int* arr, int start, int end) {
			if (start == end) {
				return new Node(arr[start]);
			}

			Node* node = new Node();
			int mid = (start + end) / 2;
			node->left = init(arr, start, mid);
			node->right = init(arr, mid + 1, end);

			node->value = min(node->left->value, node->right->value);
			return node;
		}
		int _min(Node* node, int start, int end, int left, int right) {
			if (start > right || end < left) {
				return 0; // 찾을 수 없다.
			}
			else if (start >= left && right <= end) {
				return node->value;
			}
			else {
				int mid = (start + end) / 2;
				return std::min(_min(node->left, start, mid, left, right), _min(node->right, mid + 1, end, left, right));
			}
		}
	public:
		SegmentTree(const int* arr, int n) : n(n) {
			root = init(arr, 0, n - 1);
		}
		~SegmentTree() {
			delete root;
		}
		int min(int left, int right) {
			return _min(root, 0, n-1, left, right);
		}
	};
}

namespace sumSegmentTree{
	template<typename T>
	class SumSegmentTree {
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

			node->value = node->left->value + node->right->value;
			return node;
		}
		T _sum(Node* node, int start, int end, int left, int right) {
			if ((start > right || end < left) || start > end) {
				return 0; // 찾을 수 없다.
			}
			else if (left <= start && end <= right) {
				return node->value;
			}
			else {
				int mid = (start + end) / 2;
				return _sum(node->left, start, mid, left, right) + _sum(node->right, mid + 1, end, left, right);
			}
		}
		T _update(Node* node, int start, int end, int index, T num) {
			if ((index < start || index > end) || start > end) return 0;
			if (start == end) { // index
				T diff = num - node->value;
				node->value = num;
				return diff;
			}
			else {
				int mid = (start + end) / 2;
				T diff = _update(node->left, start, mid, index, num) + _update(node->right, mid + 1, end, index, num);
				node->value += diff;
				return diff;
			}
		}
	public:
		SumSegmentTree(const T* arr, int n) : n(n) {
			root = init(arr, 0, n - 1);
		}
		~SumSegmentTree() {
			delete root;
		}
		T sum(int left, int right) {
			return _sum(root, 0, n - 1, left, right);
		}
		void update(int idx, T num) {
			_update(root, 0, n - 1, idx, num);
		}
	};

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

	class MulSegmentTree {
		class Node {
		public:
			long long value;
			Node* left;
			Node* right;
			Node(long long value) : value(value), left(NULL), right(NULL) { }
			Node() : Node(1) { }
			~Node() { delete left; delete right; }
		};
	private:
		Node* root;
		int n;
		Node* init(int start, int end) {
			Node* node = new Node();
			if (start < end) {
				int mid = (start + end) / 2;
				node->left = init(start, mid);
				node->right = init(mid + 1, end);
			}
			return node;
		}

		long long mul(Node* node, int start, int end, int left, int right) {
			if ((start > right || end < left) || start > end) {
				return 1; // 찾을 수 없다.
			}
			else if (left <= start && end <= right) {
				return node->value;
			}
			else {
				int mid = (start + end) / 2;
				return mul(node->left, start, mid, left, right) * mul(node->right, mid + 1, end, left, right);
			}
		}
		void update(Node* node, int start, int end, int idx, long long num) {
			if (start <= idx && idx <= end) {
				if (start == end) { // idx
					node->value = num;
					return;
				}

				int mid = (start + end) / 2;
				update(node->left, start, mid, idx, num);
				update(node->right, mid + 1, end, idx, num);
				node->value = node->left->value * node->right->value;
			}
		}
	public:
		MulSegmentTree(int n) : n(n) {
			root = init(0, n - 1);
		}
		~MulSegmentTree() {
			delete root;
		}
		long long mul(int left, int right) {
			return mul(root, 0, n - 1, left, right);
		}
		void update(int idx, long long num) {
			update(root, 0, n - 1, idx, num);
		}
	};

	template<typename T>
	class FenwickTree {
	private:
		vector<T> data;
	public:
		FenwickTree(const T* arr, int n) : data(n + 1) {
			for (int i = 1; i <= n; i++) {
				update(i, arr[i - 1]);
			}
		}
		FenwickTree(int n) : data(n + 1) { }
	
		long long sum(int i) {
			long long ans = 0;
			while (i > 0) {
				ans += data[i];
				i -= (i & -i); //최하위 비트 지우기
			}
			return ans;
		}
		long long sum(int left, int right) {
			return sum(right) - sum(left-1);
		}
		void update(int i, T diff) {
			while (i < data.size()) {
				data[i] += diff;
				i += (i & -i); // 최하위 비트 더하면 상위로 올라감
			}
		}
	};

	class LazySumSegmentTree {
		class Node {
		public:
			long long value;
			Node* left;
			Node* right;
			long long lazy;
			Node(long long value) : value(value), left(NULL), right(NULL), lazy(0) { }
			Node() : left(NULL), right(NULL), lazy(0) { }
			~Node() { delete left; delete right; }
			void lazyPropagate(int start, int end) {
				if (lazy != 0) {
					if (left != NULL) {
						left->lazy += lazy;
						right->lazy += lazy;
					}
					value += (end - start + 1) * lazy;
					lazy = 0;
				}
			}
		};
	private:
		Node* root;
		int n;
		Node* init(const long long* arr, int start, int end) {
			if (start == end) {
				return new Node(arr[start]);
			}

			Node* node = new Node();
			int mid = (start + end) / 2;
			node->left = init(arr, start, mid);
			node->right = init(arr, mid + 1, end);

			node->value = node->left->value + node->right->value;
			return node;
		}
		long long _sum(Node* node, int start, int end, int left, int right) {
			node->lazyPropagate(start, end);
			if ((start > right || end < left) || start > end) {
				return 0; // 찾을 수 없다.
			}
			else {
				if (left <= start && end <= right) {
					return node->value;
				}
				else {
					int mid = (start + end) / 2;
					return _sum(node->left, start, mid, left, right) + _sum(node->right, mid + 1, end, left, right);
				}
			}
		}
		void _update(Node* node, int start, int end, int left, int right, long long diff) {
			node->lazyPropagate(start, end);
			if ((start > right || end < left) || start > end) {
				// 찾을 수 없다.
			}
			else if (left <= start && end <= right) {
				node->lazy += diff;
				node->lazyPropagate(start, end);
			}
			else {
				int mid = (start + end) / 2;
				_update(node->left, start, mid, left, right, diff);
				_update(node->right, mid + 1, end, left, right, diff);
				node->value = node->left->value + node->right->value;
			}
		}
	public:
		LazySumSegmentTree(const long long* arr, int n) : n(n) {
			root = init(arr, 0, n - 1);
		}
		~LazySumSegmentTree() {
			delete root;
		}
		long long sum(int left, int right) {
			return _sum(root, 0, n - 1, left, right);
		}
		void update(int left, int right, long long diff) {
			_update(root, 0, n - 1, left, right, diff);
		}
	};

	class PersistentSegmentTree {
		class Node {
		public:
			long long value;
			int left, right;
			Node() : Node(0) { }
			Node(long long value) : value(value), left(0), right(0) { }
		};
	private:
		vector<int> roots;
		vector<Node> nodes;
		int n;
		int init(int start, int end) {
			if (start > end) {
				return 0;
			}
			else {
				int node_idx = nodes.size();
				nodes.push_back({});
				if (start < end) {
					int mid = (start + end) / 2;
					nodes[node_idx].left = init(start, mid);
					nodes[node_idx].right = init(mid + 1, end);
				}
				return node_idx;
			}
		}
		int addNode(int prev_idx, int pos, long long diff, int start, int end) {
			if (pos < start || end < pos) {
				return prev_idx;
			}

			int new_idx = nodes.size();
			nodes.push_back({ nodes[prev_idx].value + diff });

			if (start < end) {
				int mid = (start + end) / 2;
				nodes[new_idx].left = addNode(nodes[prev_idx].left, pos, diff, start, mid);
				nodes[new_idx].right = addNode(nodes[prev_idx].right, pos, diff, mid + 1, end);
			}

			return new_idx;
		}
		long long query(int node_idx, int start, int end, int left, int right) {
			if (start > end || (end < left || right < start)) {
				return 0;
			}
			else if (left <= start && end <= right) {
				return nodes[node_idx].value;
			}
			else {
				int mid = (start + end) / 2;
				return query(nodes[node_idx].left, start, mid, left, right) + query(nodes[node_idx].right, mid + 1, end, left, right);
			}
		}
		int search(int l_step_n_idx, int r_step_n_idx, int start, int end, int value) {
			if (start == end) {
				return start;
			}

			Node& l_step_node = nodes[l_step_n_idx];
			Node& r_step_node = nodes[r_step_n_idx];

			long long left_value = nodes[r_step_node.left].value - nodes[l_step_node.left].value;
			int mid = (start + end) / 2;
			if (left_value >= value) {
				return search(l_step_node.left, r_step_node.left, start, mid, value);
			}
			else {
				return search(l_step_node.right, r_step_node.right, mid + 1, end, value - left_value);
			}
		}
	public:
		PersistentSegmentTree(int n) : n(n) {
			roots.push_back(init(1, n));
			nextStep();
		}
		void addNode(int pos, long long diff) {
			roots[roots.size() - 1] = addNode(roots.back(), pos, diff, 1, n);
		}
		void nextStep() {
			roots.push_back(roots.back());
		}
		long long query(int step, int left, int right) {
			return query(roots[step], 1, n, left, right);
		}
		int search(int left_step, int right_step, int value) {
			return search(roots[left_step - 1], roots[right_step], 1, n, value);
		}
	};

	class XorPersistentSegmentTree {
		class Node {
		public:
			long long value;
			int left, right;
			Node() : Node(0) { }
			Node(long long value) : value(value), left(0), right(0) { }
		};
	private:
		vector<int> roots;
		vector<Node> nodes;
		int n;
		int init(int start, int end) {
			if (start > end) {
				return 0;
			}
			else {
				int node_idx = nodes.size();
				nodes.push_back({});
				if (start < end) {
					int mid = (start + end) / 2;
					nodes[node_idx].left = init(start, mid);
					nodes[node_idx].right = init(mid + 1, end);
				}
				return node_idx;
			}
		}
		int addNode(int prev_idx, int pos, long long diff, int start, int end) {
			if (pos < start || end < pos) {
				return prev_idx;
			}

			int new_idx = nodes.size();
			nodes.push_back({ nodes[prev_idx].value + diff });

			if (start < end) {
				int mid = (start + end) / 2;
				nodes[new_idx].left = addNode(nodes[prev_idx].left, pos, diff, start, mid);
				nodes[new_idx].right = addNode(nodes[prev_idx].right, pos, diff, mid + 1, end);
			}

			return new_idx;
		}
		long long sum(int node_idx, int start, int end, int left, int right) {
			if (start > end || (end < left || right < start)) {
				return 0;
			}
			else if (left <= start && end <= right) {
				return nodes[node_idx].value;
			}
			else {
				int mid = (start + end) / 2;
				return sum(nodes[node_idx].left, start, mid, left, right) + sum(nodes[node_idx].right, mid + 1, end, left, right);
			}
		}
		int search(int l_step_n_idx, int r_step_n_idx, int start, int end, int value, int level_bit) {
			if (start == end) {
				return start;
			}

			Node& l_step_node = nodes[l_step_n_idx];
			Node& r_step_node = nodes[r_step_n_idx];

			long long left_value = nodes[r_step_node.left].value - nodes[l_step_node.left].value;
			long long right_value = nodes[r_step_node.right].value - nodes[l_step_node.right].value;
			int mid = (start + end) / 2;
			int xor_value = value & level_bit;
			if (left_value == 0 || (right_value > 0 && xor_value == 0)) {
				return search(l_step_node.right, r_step_node.right, mid + 1, end, value, level_bit >> 1);
			}
			else {
				return search(l_step_node.left, r_step_node.left, start, mid, value, level_bit >> 1);
			}
		}
		int min(int l_step_n_idx, int r_step_n_idx, int start, int end, int value) {
			if (start == end) {
				return start;
			}

			Node& l_step_node = nodes[l_step_n_idx];
			Node& r_step_node = nodes[r_step_n_idx];

			long long left_value = nodes[r_step_node.left].value - nodes[l_step_node.left].value;
			int mid = (start + end) / 2;
			if (left_value >= value) {
				return min(l_step_node.left, r_step_node.left, start, mid, value);
			}
			else {
				return min(l_step_node.right, r_step_node.right, mid + 1, end, value - left_value);
			}
		}
	public:
		XorPersistentSegmentTree(int n) : n(n) {
			roots.push_back(init(0, n - 1));
		}
		void addNode(int pos, long long diff) {
			roots[roots.size() - 1] = addNode(roots.back(), pos, diff, 0, n - 1);
		}
		void nextStep() {
			roots.push_back(roots.back());
		}
		void reverseStep(unsigned int step) {
			if (roots.size() - 1 > step) {
				nodes.erase(nodes.begin() + roots[step + 1], nodes.end());
				roots.erase(roots.begin() + step + 1, roots.end());
			}
		}
		int getLastStep() {
			return roots.size() - 1;
		}
		long long sum(int step, int left, int right) {
			return sum(roots[step], 0, n - 1, left, right);
		}
		int search(int left_step, int right_step, int value) {
			return search(roots[left_step - 1], roots[right_step], 0, n - 1, value, n >> 1);
		}
		int min(int left_step, int right_step, int value) {
			return min(roots[left_step - 1], roots[right_step], 0, n - 1, value);
		}
	};
}