//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
//
//#define MIN(x,y) ((x > y)?(y):(x))
//#define MAX(x,y) ((x < y)?(y):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//bool fillMap(int map[][9], vector<pair<int, int>>::iterator iter, vector<pair<int, int>> &places) {
//	bool check[9];
//
//	if (iter == places.end()) {
//		return true;
//	}
//
//	memset(check, false, sizeof(bool) * 9);
//
//	// °¡·Î Å½»ö
//	for (int i = 0; i < 9; i++) {
//		if (map[i][iter->second]) {
//			check[map[i][iter->second] - 1] = true;
//		}
//	}
//
//	// ¼¼·Î Å½»ö
//	for (int i = 0; i < 9; i++) {
//		if (map[iter->first][i]) {
//			check[map[iter->first][i] - 1] = true;
//		}
//	}
//	
//	// ±¸¿ª Å½»ö
//	int tempX = iter->first / 3 * 3;
//	int tempY = iter->second / 3 * 3;
//	for (int i = tempX; i < tempX+3; i++) {
//		for (int j = tempY; j < tempY + 3; j++) {
//			if (map[i][j]) {
//				check[map[i][j] - 1] = true;
//			}
//		}
//	}
//
//	for (int i = 0; i < 9; i++) {
//		if (!check[i]) {
//			map[iter->first][iter->second] = i + 1;
//			if (fillMap(map, iter+1, places)) {
//				return true;
//			}
//		}
//	}
//
//	map[iter->first][iter->second] = 0;
//	return false;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int map[9][9];
//	vector<pair<int, int>> places;
//
//	for (int i = 0; i < 9; i++) {
//		for (int j = 0; j < 9; j++) {
//			cin >> map[i][j];
//
//			if (map[i][j] == 0) {
//				places.push_back(make_pair(i, j));
//			}
//		}
//	}
//	fillMap(map, places.begin(), places);
//
//	for (int i = 0; i < 9; i++) {
//		for (int j = 0; j < 9; j++) {
//			cout << map[i][j] << ' ';
//		}
//		cout << '\n';
//	}
//
//	return 0;
//}