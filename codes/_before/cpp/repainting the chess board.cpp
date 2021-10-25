//#include <iostream>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//
//#define MIN(x,y) ((x > y)?(y):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//int getReplaceCnt(string* board, int istart, int jstart) {
//	int bUpReplaceCnt = 0; // 좌상단이 B인 경우
//	int wUpReplaceCnt = 0; // 좌상단이 W인 경우
//
//	for (int i = istart; i < istart + 8; i++) {
//		for (int j = jstart; j < jstart + 8; j++) {
//			if ((i + j) % 2) { // 짝수 번째 인 경우
//				if (board[i][j] == 'B') {
//					bUpReplaceCnt++;
//				}
//				else {
//					wUpReplaceCnt++;
//				}
//			}else{
//				if (board[i][j] == 'B') {
//					wUpReplaceCnt++;
//				}
//				else {
//					bUpReplaceCnt++;
//				}
//			}
//		}
//	}
//
//	return MIN(bUpReplaceCnt, wUpReplaceCnt);
//}
//
//int main() {
//	int N, M;
//	int min = 1000000;
//	int cnt_temp = 0;
//
//	cin >> N >> M;
//
//	string* board = new string[N];
//
//	for (int i = 0; i < N; i++) {
//		cin >> board[i];
//	}
//
//	for (int i = 0; i < N - 8 + 1; i++) {
//		for (int j = 0; j < M - 8 + 1; j++) {
//			cnt_temp = getReplaceCnt(board, i, j);
//
//			min = MIN(cnt_temp, min);
//		}
//	}
//
//	cout << min;
//
//	return 0;
//}