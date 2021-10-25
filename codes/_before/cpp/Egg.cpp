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
//public:
//	PersistentSegmentTree(int n): n(n) {
//		roots.push_back(init(1, n));
//		nextStep();
//	}
//	void addNode(int pos, long long diff) {
//		roots[roots.size()-1] = addNode(roots.back(), pos, diff, 1, n);
//	}
//	void nextStep() {
//		roots.push_back(roots.back());
//	}
//	long long query(int step, int left, int right) {
//		return query(roots[step], 1, n, left, right);
//	}
//};
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int T;
//	cin >> T;
//	for (int t = 0; t < T; t++) {
//		int n, m;
//		cin >> n >> m;
//
//		PersistentSegmentTree tree(100001);
//
//		vector<int>* yidx = new vector<int>[100002];
//		for (int i = 0; i < n; i++) {
//			int x, y;
//			cin >> x >> y;
//			x++; y++;
//			yidx[x].push_back(y);
//		}
//
//		for (int x = 1; x <= 100001; x++) {
//			for (int y : yidx[x]) {
//				tree.addNode(y, 1);
//			}
//			tree.nextStep();
//		}
//		delete[] yidx;
//		
//		long long sum = 0;
//		for (int i = 0; i < m; i++) {
//			int e, r, b, t;
//			cin >> e >> r >> b >> t;
//			e++; r++; b++; t++;
//			sum += tree.query(r, b, t) - tree.query(e-1, b, t);
//		}
//		cout << sum << '\n';
//	}
//	
//	return 0;
//}