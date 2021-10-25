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
//void BFS(vector<vector<short>>& graph, vector<int>& inDegree, int src, int dest) {
//	int N = graph.size() - 1;
//	queue<int> q;
//	vector<int> sum(N + 1);
//	vector<bool> isVisited(N+1);
//	bool overflow = false;
//
//	// dest랑 연결이 되었는가? 안됬으면 바로 0
//	q.push(src);
//	isVisited[src] = true;
//	while (!q.empty()) {
//		int cur = q.front();
//		q.pop();
//		for (int next : graph[cur]) {
//			if (!isVisited[next]) {
//				isVisited[next] = true;
//				q.push(next);
//			}
//		}
//	}
//
//	if (!isVisited[dest]) {
//		cout << 0;
//		return;
//	}
//
//	// 혹시 src에서 갈 수 없는 노드가 있는가? 있으면 지움
//	for (int i = 1; i <= N; i++)
//		if (!isVisited[i])
//			for (int next : graph[i]) 
//				inDegree[next]--;
//
//	q.push(src);
//	sum[src] = 1;
//
//	while (!q.empty()) {
//		int cur = q.front();
//		q.pop();
//		for (int next : graph[cur]) {
//			inDegree[next]--;
//			sum[next] = sum[next] + sum[cur];
//			if (sum[next] > 1000000000) {
//				overflow = true;
//				sum[next] %= 1000000000;
//			}
//			if (inDegree[next] == 0) {
//				q.push(next);
//			}
//		}
//	}
//
//	if (inDegree[dest] > 0) {
//		cout << "inf";
//	}
//	else {
//		string str = to_string(sum[dest]);
//		if (overflow) {
//			for (int i = 0; i < 9 - str.length(); i++) {
//				cout << '0';
//			}
//		}
//		cout << str;
//	}
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int N, M;
//	cin >> N >> M;
//
//	vector<vector<short>> graph(N + 1);
//	vector<int> inDegree(N + 1);
//	for (int i = 0; i < M; i++) {
//		short f, b;
//		cin >> f >> b;
//		graph[f].push_back(b);
//		inDegree[b]++;
//	}
//	BFS(graph, inDegree, 1, 2);
//
//	return 0;
//}