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
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N, M, K;
//
//	cin >> N >> M;
//
//	int** A = new int* [N];
//	for (int i = 0; i < N; i++) {
//		A[i] = new int[M];
//
//		for (int k = 0; k < M; k++) {
//			cin >> A[i][k];
//		}
//	}
//
//	cin >> M >> K;
//	int** B = new int* [M];
//	for (int i = 0; i < M; i++) {
//		B[i] = new int[K];
//
//		for (int k = 0; k < K; k++) {
//			cin >> B[i][k];
//		}
//	}
//
//	int** C = new int* [N];
//	for (int i = 0; i < N; i++) {
//		C[i] = new int[K];
//		
//		for (int k = 0; k < K; k++) {
//			C[i][k] = 0;
//			for (int m = 0; m < M; m++) {
//				C[i][k] += A[i][m] * B[m][k];
//			}
//		}
//	}
//
//	for (int i = 0; i < N; i++) {
//		for (int k = 0; k < K; k++) {
//			cout << C[i][k] << ' ';
//		}
//		cout << '\n';
//	}
//
//	// 1 2 
//	// 3 4
//	// 5 6
//
//	// -1 -2 0
//	// 0 0 3
//
//	return 0;
//}