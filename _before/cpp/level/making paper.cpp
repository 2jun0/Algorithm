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
//	white = 0x01, blue = 0x10, complicate = 0x11
//};
//
//inline return_type operator | (return_type lhs, return_type rhs) {
//	return (return_type)((int)lhs | (int)rhs);
//}
//
//return_type getPaperCnt(bool** color, int startRow, int startCol, int endRow, int endCol, int& whiteCnt, int&blueCnt) {
//	if (startRow == endRow) { // 1size
//		if (color[startRow][startCol]) {
//			blueCnt++;
//			return return_type::blue;
//		}
//		else {
//			whiteCnt++;
//			return return_type::white;
//		}
//	}
//
//	int pinRow = (endRow - startRow) / 2 + startRow;
//	int pinCol = (endCol - startCol) / 2 + startCol;
//
//	return_type type = getPaperCnt(color, startRow, startCol, pinRow, pinCol, whiteCnt, blueCnt) |
//	getPaperCnt(color, pinRow+1, startCol, endRow, pinCol, whiteCnt, blueCnt) |
//	getPaperCnt(color, startRow, pinCol+1, pinRow, endCol, whiteCnt, blueCnt) |
//	getPaperCnt(color, pinRow+1, pinCol+1, endRow, endCol, whiteCnt, blueCnt);
//
//	switch (type)
//	{
//	case return_type::white:
//		whiteCnt -= 3;
//		return return_type::white;
//	case return_type::blue:
//		blueCnt -= 3;
//		return return_type::blue;
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
//	bool** color = new bool* [N];
//	for (int i = 0; i < N; i++) {
//		color[i] = new bool[N];
//		for (int k = 0; k < N; k++) {
//			cin >> color[i][k];
//		}
//	}
//
//	int whiteCnt = 0;
//	int blueCnt = 0;
//	getPaperCnt(color, 0, 0, N - 1, N - 1, whiteCnt, blueCnt);
//
//	cout << whiteCnt << "\n" << blueCnt;
//
//	return 0;
//}