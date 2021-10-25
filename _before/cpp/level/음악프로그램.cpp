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
//void BFS(vector<int>& inDegree, vector<set<int>>& graph) {
//	vector<bool> isVisited(graph.size());
//	queue<int> q;
//	queue<int> result;
//	for (int i = 1; i < inDegree.size(); i++)
//		if (inDegree[i] == 0) {
//			q.push(i);
//		}
//
//	while (!q.empty()) {
//		int cur = q.front();
//
//		q.pop();
//
//		result.push(cur);
//		if (isVisited[cur]) {
//			cout << 0;
//			return;
//		}
//		isVisited[cur] = true;
//
//		for (int i : graph[cur]) {
//			inDegree[i]--;
//
//			if (inDegree[i] == 0)
//				q.push(i);
//		}
//	}
//
//	for (int i = 1; i < isVisited.size(); i++)
//		if (!isVisited[i]) {
//			cout << 0;
//			return;
//		}
//
//	while(!result.empty()){
//		cout << result.front() << '\n';
//		result.pop();
//	}
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int N, K;
//	cin >> N >> K;
//
//	vector<int> inDegree(N + 1);
//	vector<set<int>> graph(N + 1);
//
//	for (int _ = 0; _ < K; _++) {
//		int M;
//		cin >> M;
//
//		int f, b;
//		cin >> f;
//		for (int i = 1; i < M; i++) {
//			cin >> b;
//			if (!graph[f].count(b)) {
//				graph[f].insert(b);
//				inDegree[b]++;
//			}
//			f = b;
//		}
//	}
//
//	BFS(inDegree, graph);
//
//	return 0;
//}