//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
//#include <set>
//#include <queue>
//
//#define ABS(x) (((x) < 0)?-(x):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//enum class return_type {
//	minus = 0x001, zero = 0x010, plus = 0x100, complicate = 0x111
//};
//
//inline return_type operator | (return_type lhs, return_type rhs) {
//	return (return_type)((int)lhs | (int)rhs);
//}
//
//return_type getPaperCnt(short** color, int startRow, int startCol, int endRow, int endCol, int* cnt) {
//	if (startRow == endRow) { // 1size
//		if (color[startRow][startCol] == -1) {
//			cnt[0]++;
//			return return_type::minus;
//		}
//		else if (color[startRow][startCol] == 0) {
//			cnt[1]++;
//			return return_type::zero;
//		}
//		else if (color[startRow][startCol] == 1) {
//			cnt[2]++;
//			return return_type::plus;
//		}
//	}
//
//	int pinRow1 = (endRow - startRow + 1) / 3 - 1 + startRow;
//	int pinRow2 = (endRow - startRow + 1) / 3 * 2 - 1 + startRow;
//	int pinCol1 = (endCol - startCol + 1) / 3 - 1 + startCol;
//	int pinCol2 = (endCol - startCol + 1) / 3 * 2 - 1 + startCol;
//
//	return_type type = getPaperCnt(color, startRow, startCol, pinRow1, pinCol1, cnt) |
//		getPaperCnt(color, startRow, pinCol1 + 1, pinRow1, pinCol2, cnt) |
//		getPaperCnt(color, startRow, pinCol2 + 1, pinRow1, endCol, cnt) |
//		getPaperCnt(color, pinRow1 + 1, startCol, pinRow2, pinCol1, cnt) |
//		getPaperCnt(color, pinRow1 + 1, pinCol1 + 1, pinRow2, pinCol2, cnt) |
//		getPaperCnt(color, pinRow1 + 1, pinCol2 + 1, pinRow2, endCol, cnt) |
//		getPaperCnt(color, pinRow2 + 1, startCol, endRow, pinCol1, cnt) |
//		getPaperCnt(color, pinRow2 + 1, pinCol1 + 1, endRow, pinCol2, cnt) |
//		getPaperCnt(color, pinRow2 + 1, pinCol2 + 1, endRow, endCol, cnt);
//
//	switch (type)
//	{
//	case return_type::minus:
//		cnt[0]-=8;
//		return return_type::minus;
//	case return_type::zero:
//		cnt[1]-=8;
//		return return_type::zero;
//	case return_type::plus:
//		cnt[2]-=8;
//		return return_type::plus;
//	case return_type::complicate:
//		return return_type::complicate;
//	}
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N;
//	cin >> N;
//
//	short** color = new short* [N];
//	for (int i = 0; i < N; i++) {
//		color[i] = new short[N];
//		for (int k = 0; k < N; k++) {
//			cin >> color[i][k];
//		}
//	}
//
//	int cnt[3];
//	cnt[0] = 0;
//	cnt[1] = 0;
//	cnt[2] = 0;
//	getPaperCnt(color, 0, 0, N - 1, N - 1, cnt);
//
//	cout << cnt[0] << "\n" << cnt[1] << "\n" << cnt[2];
//
//	for (int i = 0; i < N; i++) {
//		delete[] color[i];
//	}
//	delete[] color;
//
//	return 0;
//}