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
//	stack<int> result;
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
//			cout << "IMPOSSIBLE";
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
//			cout << "IMPOSSIBLE";
//			return;
//		}
//
//	while (!result.empty()) {
//		cout << result.top() << ' ';
//		result.pop();
//	}
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int T;
//	cin >> T;
//
//	for (int t = 0; t < T; t++) {
//		int N;
//		cin >> N;
//
//		vector<int> inDegree(N + 1);
//		vector<set<int>> graph(N + 1);
//
//		vector<int> nums(N);
//		for (int i = 0; i < N; i++) {
//			cin >> nums[i];
//
//			for (int k = 0; k < i; k++) {
//				inDegree[nums[k]]++;
//				graph[nums[i]].insert(nums[k]);
//			}
//		}
//
//		int M;
//		cin >> M;
//		for (int i = 0; i < M; i++) {
//			int a, b;
//			// a -> b 를 기준으로 함.
//			cin >> a >> b;
//
//			if (graph[b].count(a) > 0) { // b -> a인 경우
//				swap(a, b);
//			}
//
//			inDegree[b]--;
//			graph[a].erase(b);
//			inDegree[a]++;
//			graph[b].insert(a);
//		}
//
//		BFS(inDegree, graph);
//		cout << '\n';
//	}
//
//	return 0;
//}