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
//void BFS(vector<int>& inDegree, vector<vector<int>> graph, int N) {
//	queue<int> q;
//	for (int i = 1; i <= N; i++)
//		if (inDegree[i] == 0)
//			q.push(i);
//
//	while (!q.empty()) {
//		int cur = q.front();
//		q.pop();
//
//		cout << cur << " ";
//		for (int i : graph[cur]) {
//			inDegree[i]--;
//			if (inDegree[i] == 0)
//				q.push(i);
//		}
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
//	vector<int> inDegree(N+1);
//	vector<vector<int>> graph(N + 1);
//
//	for (int i = 0; i < M; i++)	{
//		int f, b;
//		cin >> f >> b;
//
//		graph[f].push_back(b);
//		inDegree[b]++;
//	}
//
//	BFS(inDegree, graph, N);
//	return 0;
//}