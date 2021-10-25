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
//bool search(char** arr, int** flag, int R, int C, int r, int c, int f, int cnts[2]) {
//	if ((c < 0 || c >= C) || (r < 0 || r >= R)) return false;
//	if (flag[r][c] != 0) return false;
//	if (arr[r][c] == 'o') cnts[0] ++;
//	if (arr[r][c] == 'v') cnts[1] ++;
//	flag[r][c] = f;
//	search(arr, flag, R, C, r, c + 1, f, cnts);
//	search(arr, flag, R, C, r, c - 1, f, cnts);
//	search(arr, flag, R, C, r + 1, c, f, cnts);
//	search(arr, flag, R, C, r - 1, c, f, cnts);
//	return true;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int R, C;
//	cin >> R >> C;
//
//	char** arr = new char*[R];
//	for (int r = 0; r < R; r++) {
//		arr[r] = new char[C+1];
//		cin >> arr[r];
//	}
//
//	int** flag = new int*[R];
//	for (int r = 0; r < R; r++) {
//		flag[r] = new int[C];
//		memset(flag[r], 0, sizeof(int) * C);
//		for (int c = 0; c < C; c++) {
//			if (arr[r][c] == '#') {
//				flag[r][c] = -1;
//			}
//		}
//	}
//
//	int cnts[2];
//
//	int flag_cnt = 0;
//
//	int sheep_cnt = 0;
//	int wolf_cnt = 0;
//	for (int r = 0; r < R; r++) {
//		for (int c = 0; c < C; c++) {
//			cnts[0] = 0; cnts[1] = 0;
//			if (search(arr, flag, R, C, r, c, flag_cnt + 1, cnts)) {
//				flag_cnt++;
//			}
//			if (cnts[0] > cnts[1]) {
//				sheep_cnt += cnts[0];
//			}
//			else {
//				wolf_cnt += cnts[1];
//			}
//		}
//	}
//
//	cout << sheep_cnt << ' ' << wolf_cnt;
//
//	for (int r = 0; r < R; r++) {
//		delete[] arr[r];
//		delete[] flag[r];
//	}
//	delete[] arr;
//	delete[] flag;
//
//	return 0;
//}