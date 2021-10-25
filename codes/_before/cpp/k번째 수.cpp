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
//class PersistentSegmentTree {
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
//	long long query(int node_idx, int start, int end, int left, int right) {
//		if (start > end || (end < left || right < start)) {
//			return 0;
//		}
//		else if (left <= start && end <= right) {
//			return nodes[node_idx].value;
//		}
//		else {
//			int mid = (start + end) / 2;
//			return query(nodes[node_idx].left, start, mid, left, right) + query(nodes[node_idx].right, mid + 1, end, left, right);
//		}
//	}
//	int search(int l_step_n_idx, int r_step_n_idx, int start, int end, int value) {
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
//			return search(l_step_node.left, r_step_node.left, start, mid, value);
//		}
//		else {
//			return search(l_step_node.right, r_step_node.right, mid + 1, end, value - left_value);
//		}
//	}
//public:
//	PersistentSegmentTree(int n) : n(n) {
//		roots.push_back(init(1, n));
//		nextStep();
//	}
//	void addNode(int pos, long long diff) {
//		roots[roots.size() - 1] = addNode(roots.back(), pos, diff, 1, n);
//	}
//	void nextStep() {
//		roots.push_back(roots.back());
//	}
//	long long query(int step, int left, int right) {
//		return query(roots[step], 1, n, left, right);
//	}
//	int search(int left_step, int right_step, int value) {
//		return search(roots[left_step-1], roots[right_step], 1, n, value);
//	}
//};
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int n, m;
//	cin >> n >> m;
//
//	PersistentSegmentTree tree(n);
//
//	long long* ys = new long long[n];
//	for (int i = 0; i < n; i++) {
//		cin >> ys[i];
//	}
//
//	long long* sortedYs = new long long[n];
//	memcpy(sortedYs, ys, sizeof(long long) * n);
//	mergeSort(sortedYs, 0, n-1);
//
//	// 각 y에 대한 index를 assign
//	// 곂치는 수가 없으므로 중복을 생각하지 않아도 괜찮다.
//	vector<int> idxYToY(n+1);
//	map<long long, int> yToIdxY;
//	for (int i = 0; i < n; i++) {
//		idxYToY[i + 1] = sortedYs[i];
//		yToIdxY[sortedYs[i]] = i + 1;
//	}
//	delete[] sortedYs;
//
//	// y를 index로 변환
//	vector<long long> idxYs(n);
//	for (int i = 0; i < n; i++) {
//		idxYs[i] = yToIdxY[ys[i]];
//	}
//	delete[] ys;
//	
//	for (long long idxY : idxYs) {
//		tree.addNode(idxY, 1);
//		tree.nextStep();
//	}
//
//	for (int _ = 0; _ < m; _++) {
//		int i, j, k;
//		cin >> i >> j >> k;
//		cout << idxYToY[tree.search(i, j, k)] << '\n';
//	}
//
//	return 0;
//}