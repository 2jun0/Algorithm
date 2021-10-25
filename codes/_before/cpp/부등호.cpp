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
//void BFS(vector<int>& inDegree, vector<vector<int>>& graph, vector<int>& result, bool isMax) {
//	priority_queue<int, vector<int>, greater<int> > q;
//	int minV = 0;
//	int maxV = 9;
//	for (int i = 1; i < inDegree.size(); i++)
//		if (inDegree[i] == 0)
//			q.push(i);
//
//	while (!q.empty()) {
//		int cur = q.top();
//		q.pop();
//
//		if(isMax) result[cur] = maxV--;
//		else result[cur] = minV++;
//		for (int i : graph[cur]) {
//			inDegree[i]--;
//			if (inDegree[i] == 0) {
//				q.push(i);
//			}
//		}
//	}
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int N;
//	cin >> N;
//
//	vector<char> cs(N+1);
//	for (int i = 1; i <= N; i++) {
//		cin >> cs[i];
//	}
//
//	vector<int> inDegree(N+2);
//	vector<vector<int>> graph(N+2);
//	vector<int> result(N+2);
//
//	for (int i = 1; i <= N; i++) {
//		if (cs[i] == '>') {
//			graph[i].push_back(i+1);
//			inDegree[i + 1]++;
//		}
//		else {
//			graph[i + 1].push_back(i);
//			inDegree[i]++;
//		}
//	}
//
//	BFS(inDegree, graph, result, true);
//
//	for (int i = 1; i < result.size(); i++) {
//		cout << result[i];
//	}
//	cout << '\n';
//
//	vector<int> inDegree2(N + 2);
//	vector<vector<int>> graph2(N + 2);
//	for (int i = 1; i <= N; i++) {
//		if (cs[i] == '>') {
//			graph2[i + 1].push_back(i);
//			inDegree2[i]++;
//		}
//		else {
//			graph2[i].push_back(i + 1);
//			inDegree2[i + 1]++;
//		}
//	}
//
//	BFS(inDegree2, graph2, result, false);
//	for (int i = 1; i < result.size(); i++) {
//		cout << result[i];
//	}
//
//	return 0;
//}