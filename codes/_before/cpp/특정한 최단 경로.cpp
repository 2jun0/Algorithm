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
//class DijkstraNode {
//public:
//	int cur;
//	long long distance;
//	int prev;
//	DijkstraNode(int cur, long long distance, int prev) : cur(cur), distance(distance), prev(prev) {}
//};
//
//class Line {
//public:
//	int dest;
//	int distance;
//	Line(int dest, int distance) : dest(dest), distance(distance) {}
//};
//
//struct cmp {
//	bool operator()(const DijkstraNode& a, const DijkstraNode& b) {
//		 return a.distance > b.distance;
//	}
//};
//
//int dijkstra(vector<vector<Line>>& graph, int src, int dest) {
//	priority_queue<DijkstraNode, vector<DijkstraNode>, cmp > pq;
//	/*for (int i = 1; i < graph.size(); i++) {
//		if (i == src) pq.push({ i, 0, -1 });
//		else pq.push({ i, -1, -1 });
//	}*/
//	pq.push({ src, 0, -1 });
//
//	vector<long long> shortestDistances(graph.size(), -1);
//	shortestDistances[src] = 0;
//
//	while (!pq.empty()) {
//		DijkstraNode node = pq.top();
//		pq.pop();
//
//		for (Line& line : graph[node.cur]) {
//			if (shortestDistances[line.dest] == -1 || shortestDistances[line.dest] > line.distance + node.distance) {
//				shortestDistances[line.dest] = line.distance + node.distance;
//				pq.push({ line.dest, shortestDistances[line.dest], node.cur });
//			}
//		}
//	}
//
//	return shortestDistances[dest];
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int N, E;
//	cin >> N >> E;
//
//	vector<vector<Line>> graph(N + 1);
//
//	for (int i = 0; i < E; i++)	{
//		int f, b, d;
//		cin >> f >> b >> d;
//
//		graph[f].push_back({ b, d });
//		graph[b].push_back({ f, d });
//	}
//
//	int v1, v2;
//	cin >> v1 >> v2;
//
//	long long a1 = dijkstra(graph, 1, v1);
//	long long a2 = dijkstra(graph, 1, v2);
//	long long b = dijkstra(graph, v1, v2);
//	long long c1 = dijkstra(graph, v2, N);
//	long long c2 = dijkstra(graph, v1, N);
//
//	if (b == -1) {
//		cout << -1;
//	}else if (a1 + c1 < a2 + c2) {
//		if (a1 == -1 || c1 == -1) cout << -1;
//		else cout << a1 + b + c1;
//	}
//	else {
//		if (a2 == -1 || c2 == -1) cout << -1;
//		else cout << a2 + b + c2;
//	}
//
//	return 0;
//}