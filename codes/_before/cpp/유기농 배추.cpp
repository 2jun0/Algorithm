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
//bool search(int** arr, bool** flag, int R, int C, int r, int c) {
//	if ((c < 0 || c >= C) || (r < 0 || r >= R)) return false;
//	if (flag[r][c] || arr[r][c] == 0) return false;
//	flag[r][c] = true;
//	search(arr, flag, R, C, r, c + 1);
//	search(arr, flag, R, C, r, c - 1);
//	search(arr, flag, R, C, r + 1, c);
//	search(arr, flag, R, C, r - 1, c);
//	return true;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int T;
//	cin >> T;
//	for (int t = 0; t < T; t++)	{
//		int M, N, K;
//		cin >> M >> N >> K;
//		int** plants = new int* [N];
//		bool** flag = new bool* [N];
//		for (int i = 0; i < N; i++) {
//			plants[i] = new int[M];
//			flag[i] = new bool[M];
//			memset(plants[i], 0, sizeof(int) * M);
//			memset(flag [i] , false, sizeof(bool) * M);
//		}
//
//		for (int k = 0; k < K; k++) {
//			int x, y;
//			cin >> x >> y;
//			plants[y][x] = 1;
//		}
//
//		int cnt = 0;
//		for (int i = 0; i < N; i++) {
//			for (int j = 0; j < M; j++) {
//				if (search(plants, flag, N, M, i, j)) {
//					cnt++;
//				}
//			}
//		}
//
//		cout << cnt << '\n';
//
//		for (int i = 0; i < N; i++) {
//			delete[] plants[i];
//			delete[] flag[i];
//		}
//		delete[] plants;
//	}
//	return 0;
//}