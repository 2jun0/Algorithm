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
//class XorPersistentSegmentTree {
//	class Node {
//	public:
//		long long value;
//		int left, right;
//		Node() : Node(0) { }
//		Node(long long value) : value(value), left(0), right(0) { }
//	};
//private:
//	vector<int> roots;
//	vector<Node> nodes;
//	int n;
//	int init(int start, int end) {
//		if (start > end) {
//			return 0;
//		}
//		else {
//			int node_idx = nodes.size();
//			nodes.push_back({});
//			if (start < end) {
//				int mid = (start + end) / 2;
//				nodes[node_idx].left = init(start, mid);
//				nodes[node_idx].right = init(mid + 1, end);
//			}
//			return node_idx;
//		}
//	}
//	int addNode(int prev_idx, int pos, long long diff, int start, int end) {
//		if (pos < start || end < pos) {
//			return prev_idx;
//		}
//
//		int new_idx = nodes.size();
//		nodes.push_back({ nodes[prev_idx].value + diff });
//
//		if (start < end) {
//			int mid = (start + end) / 2;
//			nodes[new_idx].left = addNode(nodes[prev_idx].left, pos, diff, start, mid);
//			nodes[new_idx].right = addNode(nodes[prev_idx].right, pos, diff, mid + 1, end);
//		}
//
//		return new_idx;
//	}
//	long long sum(int node_idx, int start, int end, int left, int right) {
//		if (start > end || (end < left || right < start)) {
//			return 0;
//		}
//		else if (left <= start && end <= right) {
//			return nodes[node_idx].value;
//		}
//		else {
//			int mid = (start + end) / 2;
//			return sum(nodes[node_idx].left, start, mid, left, right) + sum(nodes[node_idx].right, mid + 1, end, left, right);
//		}
//	}
//	int search(int l_step_n_idx, int r_step_n_idx, int start, int end, int value, int level_bit) {
//		if (start == end) {
//			return start;
//		}
//
//		Node& l_step_node = nodes[l_step_n_idx];
//		Node& r_step_node = nodes[r_step_n_idx];
//
//		long long left_value = nodes[r_step_node.left].value - nodes[l_step_node.left].value;
//		long long right_value = nodes[r_step_node.right].value - nodes[l_step_node.right].value;
//		int mid = (start + end) / 2;
//		int xor_value = value & level_bit;
//		if (left_value == 0 || (right_value > 0 && xor_value == 0)) {
//			return search(l_step_node.right, r_step_node.right, mid + 1, end, value, level_bit>>1);
//		}
//		else {
//			return search(l_step_node.left, r_step_node.left, start, mid, value, level_bit>>1);
//		}
//	}
//	int min(int l_step_n_idx, int r_step_n_idx, int start, int end, int value) {
//		if (start == end) {
//			return start;
//		}
//
//		Node& l_step_node = nodes[l_step_n_idx];
//		Node& r_step_node = nodes[r_step_n_idx];
//
//		long long left_value = nodes[r_step_node.left].value - nodes[l_step_node.left].value;
//		int mid = (start + end) / 2;
//		if (left_value >= value) {
//			return min(l_step_node.left, r_step_node.left, start, mid, value);
//		}
//		else {
//			return min(l_step_node.right, r_step_node.right, mid + 1, end, value - left_value);
//		}
//	}
//public:
//	XorPersistentSegmentTree(int n) : n(n) {
//		roots.push_back(init(0, n-1));
//	}
//	void addNode(int pos, long long diff) {
//		roots[roots.size() - 1] = addNode(roots.back(), pos, diff, 0, n-1);
//	}
//	void nextStep() {
//		roots.push_back(roots.back());
//	}
//	void reverseStep(unsigned int step) {
//		if (roots.size() - 1 > step) {
//			nodes.erase(nodes.begin() + roots[step + 1], nodes.end());
//			roots.erase(roots.begin() + step + 1, roots.end());
//		}
//	}
//	int getLastStep() {
//		return roots.size() - 1;
//	}
//	long long sum(int step, int left, int right) {
//		return sum(roots[step], 0, n-1, left, right);
//	}
//	int search(int left_step, int right_step, int value) {
//		return search(roots[left_step - 1], roots[right_step], 0, n-1, value, n>>1);
//	}
//	int min(int left_step, int right_step, int value) { 
//		return min(roots[left_step - 1], roots[right_step], 0, n-1, value);
//	}
//};
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	XorPersistentSegmentTree tree(524288);
//
//	int m;
//	cin >> m;
//
//	vector<int> nums;
//	for (int i = 0; i < m; i++) {
//		int type;
//		cin >> type;
//		switch (type) {
//			int L, R, x, k;
//		case 1:
//			cin >> x;
//			tree.nextStep();
//			nums.push_back(x);
//			tree.addNode(x, 1);
//			break;
//		case 2:
//			cin >> L >> R >> x;
//			cout << tree.search(L, R, x) << '\n';
//			break;
//		case 3:
//			cin >> k;
//			tree.reverseStep(tree.getLastStep() - k);
//			break;
//		case 4:
//			cin >> L >> R >> x;
//			cout << tree.sum(R, 1, x) - tree.sum(L - 1, 1, x) << '\n';
//			break;
//		case 5:
//			cin >> L >> R >> k;
//			cout << tree.min(L, R, k) << '\n';
//			break;
//		}
//	}
//
//	return 0;
//}