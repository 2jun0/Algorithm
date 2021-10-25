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
//	white = 0x01, black = 0x10, complicate = 0x11
//};
//
//inline return_type operator | (return_type lhs, return_type rhs) {
//	return (return_type)((int)lhs | (int)rhs);
//}
//
//string getQuadTree(bool** color, int startRow, int startCol, int endRow, int endCol, return_type& returnType) {
//	if (startRow == endRow) { // 1size
//		if (color[startRow][startCol]) {
//			returnType = return_type::black;
//			return "1";
//		}
//		else {
//			returnType = return_type::white;
//			return "0";
//		}
//	}
//
//	int pinRow = (endRow - startRow) / 2 + startRow;
//	int pinCol = (endCol - startCol) / 2 + startCol;
//
//	string str = "(";
//	return_type type;
//	return_type type_temp;
//	str += getQuadTree(color, startRow, startCol, pinRow, pinCol, type);
//	str += getQuadTree(color, startRow, pinCol + 1, pinRow, endCol, type_temp);
//	type = type | type_temp;
//	str += getQuadTree(color, pinRow + 1, startCol, endRow, pinCol, type_temp);
//	type = type | type_temp;
//	str += getQuadTree(color, pinRow + 1, pinCol + 1, endRow, endCol, type_temp);
//	type = type | type_temp;
//	str += ")";
//
//	switch (type)
//	{
//	case return_type::white:
//		returnType = return_type::white;
//		return "0";
//	case return_type::black:
//		returnType = return_type::black;
//		return "1";
//	case return_type::complicate:
//		returnType = return_type::complicate;
//		return str;
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
//
//		string line;
//		cin >> line;
//		for (int k = 0; k < N; k++) {
//			color[i][k] = line[k]=='1';
//		}
//	}
//
//	return_type temp;
//	cout << getQuadTree(color, 0, 0, N - 1, N - 1, temp);
//	return 0;
//}