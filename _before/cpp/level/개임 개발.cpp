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
//void BFS(vector<int>& inDegree, vector<vector<int>> graph, vector<int> delay) {
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
//	for (int i = 1; i < sum_delay.size(); i++) {
//		cout << sum_delay[i] << '\n';
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
//	vector<int> delay(N + 1);
//	vector<int> inDegree(N + 1);
//	vector<vector<int>> graph(N + 1);
//
//	for (int i = 1; i <= N; i++) {
//		cin >> delay[i];
//
//		int f;
//		cin >> f;
//
//		while (f != -1) {
//			graph[f].push_back(i);
//			inDegree[i]++;
//			cin >> f;
//		}
//	}
//
//	BFS(inDegree, graph, delay);
//	
//	return 0;
//}