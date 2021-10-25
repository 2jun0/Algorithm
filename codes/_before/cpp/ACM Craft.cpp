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
//int BFS(vector<int>& inDegree, vector<vector<int>> graph, vector<int> delay, int dest) {
//	queue<int> q;
//	vector<int> sum_delay(delay.size());
//	for (int i = 1; i < inDegree.size(); i++)
//		if (inDegree[i] == 0) {
//			sum_delay[i] = delay[i];
//			q.push(i);
//		}
//
//	while (!q.empty()) {
//		int cur = q.front();
//		if (dest == cur) {
//			return sum_delay[cur];
//		}
//
//		q.pop();
//		
//		for (int i : graph[cur]) {
//			inDegree[i]--;
//
//			sum_delay[i] = max(sum_delay[i], delay[i] + sum_delay[cur]);
//			if (inDegree[i] == 0)
//				q.push(i);
//		}
//	}
//
//	return -1;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int T;
//	cin >> T;
//	for (int t = 0; t < T; t++)	{
//		int N, K;
//		cin >> N >> K;
//
//		vector<int> delay(N + 1);
//		for (int i = 1; i <= N; i++) {
//			cin >> delay[i];
//		}
//
//		vector<int> inDegree(N + 1);
//		vector<vector<int>> graph(N + 1);
//
//		for (int i = 0; i < K; i++) {
//			int f, b;
//			cin >> f >> b;
//
//			graph[f].push_back(b);
//			inDegree[b]++;
//		}
//		int dest;
//		cin >> dest;
//
//		cout << BFS(inDegree, graph, delay, dest) << '\n';
//	}
//	
//	return 0;
//}