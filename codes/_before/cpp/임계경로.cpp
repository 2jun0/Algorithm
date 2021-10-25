//#include <iostream>
//#include <cstring>
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
//class Line {
//public:
//	int dest;
//	int delay;
//	Line() {}
//	Line(int dest, int delay): dest(dest), delay(delay) {}
//};
//
//void BFS(vector<int>& inDegree, vector<vector<Line>>& graph, vector<vector<Line>>& rgraph, int src, int dest) {
//	queue<int> q;
//	vector<int> sum_delay(graph.size());
//
//	q.push(src);
//	while (!q.empty()) {
//		int cur = q.front();
//
//		q.pop();
//
//		for (Line& line : graph[cur]) {
//			inDegree[line.dest]--;
//
//			if (sum_delay[line.dest] < line.delay + sum_delay[cur]) {
//				sum_delay[line.dest] = line.delay + sum_delay[cur];
//			}
//
//			if (inDegree[line.dest] == 0) {
//				q.push(line.dest);
//			}
//		}
//	}
//
//	q.push(dest);
//	vector<bool> isVisited(graph.size());
//	int count = 0;
//	while (!q.empty()) {
//		int cur = q.front();
//
//		q.pop();
//
//		for (Line& line : rgraph[cur]) {
//			if (sum_delay[line.dest] == sum_delay[cur] - line.delay) {
//				count++;
//				if (!isVisited[line.dest]) {
//					q.push(line.dest);
//					isVisited[line.dest] = true;
//				}
//			}
//		}
//	}
//
//	cout << sum_delay[dest] << '\n' << count;
//}
//
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int N, M;
//	cin >> N >> M;
//
//	vector<int> inDegree(N + 1);
//	vector<vector<Line>> graph(N + 1);
//	vector<vector<Line>> rgraph(N + 1);
//
//	for (int i = 0; i < M; i++) {
//		int f, b, d;
//		cin >> f >> b >> d;
//
//		inDegree[b]++;
//		graph[f].push_back({ b, d });
//
//		rgraph[b].push_back({ f, d });
//	}
//
//	int src, dest;
//	cin >> src >> dest;
//
//	BFS(inDegree, graph, rgraph, src, dest);
//
//	return 0;
//}