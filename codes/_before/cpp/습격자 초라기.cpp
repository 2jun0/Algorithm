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
//class Node {
//public:
//	int pos;
//	vector<Node&> connectedNodes;
//	Node(int pos) : pos(pos) {}
//	void deconnect(int pos) {
//		for (vector<Node&>::iterator iter = connectedNodes.begin(); iter != connectedNodes.end(); iter++) {
//			iter.
//		}
//	}
//	void deconnectAll() {
//		for (Node& node : connectedNodes) {
//			node.deconnect(pos);
//		}
//	}
//};
//
//struct cmp {
//	bool operator()(const Node& a, const Node& b) {
//		return a.connectedNodes.size() > b.connectedNodes.size();
//	}
//};
//
//int dinamic(vector<int> outer, vector<int> inner, int W) {
//	int N = outer.size();
//	vector<Node> nodes(N*2);
//
//	for (int i = 0; i < N; i++) {
//		nodes[i] = i;
//
//		int left = (i == 0) ? N - 1 : i - 1;
//		int right = (i == N - 1) ? 0 : i + 1;
//		if (outer[i] + outer[left] <= W) {
//			nodes[i].connectedNodes.push_back(nodes[left]);
//		}
//		if (outer[i] + outer[right] <= W) {
//			nodes[i].connectedNodes.push_back(nodes[right]);
//		}
//		if (outer[i] + inner[i] <= W) {
//			nodes[i].connectedNodes.push_back(nodes[i + N]);
//		}
//	}
//
//	for (int i = 0; i < N; i++) {
//		nodes[i+N] = i+N;
//
//		int left = (i == 0) ? N - 1 : i - 1;
//		int right = (i == N - 1) ? 0 : i + 1;
//		if (inner[i] + inner[left] <= W) {
//			nodes[i + N].connectedNodes.push_back(nodes[left + N]);
//		}
//		if (inner[i] + inner[right] <= W) {
//			nodes[i + N].connectedNodes.push_back(nodes[right + N]);
//		}
//		if (inner[i] + outer[i] <= W) {
//			nodes[i + N].connectedNodes.push_back(nodes[i]);
//		}
//	}
//
//	priority_queue<Node&, vector<Node&>, cmp > pq;
//	for (int i = 0; i < N * 2; i++) pq.push(nodes[i]);
//
//	while (!pq.empty()) {
//		Node& node = pq.top();
//		node.pos
//		pq.
//		pq.pop();
//	}
//
//	return shortestDistances[dest];
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int T;
//	cin >> T;
//
//	for (int _ = 0; _ < T; _++) {
//		int N, W;
//		cin >> N >> W;
//		vector<int> outer(N);
//		vector<int> inner(N);
//
//		for (int i = 0; i < N; i++) {
//			cin >> outer[i];
//		}
//		for (int i = 0; i < N; i++) {
//			cin >> inner[i];
//		}
//
//		dinamic(outer, inner, W);
//	}
//
//	return 0;
//}