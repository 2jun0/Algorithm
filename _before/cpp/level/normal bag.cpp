//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
//#include <set>
//
//#define ABS(x) (((x) < 0)?-(x):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//int knapsack(int limit, int* weights, int* values, int n) {
//	int** V = new int*[n+1];
//
//	// V init
//	V[0] = new int[limit+1];
//	memset(V[0], 0, sizeof(int) * (limit + 1));
//
//	for (int i = 1; i <= n; i++) {
//		V[i] = new int[limit+1];
//
//		memcpy(V[i], V[i - 1], sizeof(int) * (limit + 1)); // 이전의 기록 복붙
//
//		for (int k  = weights[i-1]; k <= limit; k++) {
//			V[i][k] = max(V[i][k], values[i - 1] + V[i - 1][k - weights[i - 1]]);
//		}
//
//		delete[] V[i - 1];
//	}
//
//	int max = V[n][limit];
//	delete[] V[n];
//	delete[] V;
//
//	return max;
//}
//
//int main() {
//	int N, K;
//	cin >> N >> K;
//
//	int* weights = new int[N];
//	int* values = new int[N];
//
//	for (int i = 0; i < N; i++) {
//		cin >> weights[i] >> values[i];
//	}
//
//	cout << knapsack(K, weights, values, N);
//
//	return 0;
//}