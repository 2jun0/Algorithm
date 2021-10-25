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
//int getQueenCaseCnt(int depth, vector<pair<int, int>> &queens, int n) {
//	vector<pair<int, int>>::iterator iter;
//	bool isCollision = false;
//	int cnt = 0;
//
//	if (depth == n) {
//		return 1;
//	}
//
//	for (int i = 0; i < n; i++) {
//		isCollision = false;
//		// collision check
//		for (iter = queens.begin(); iter != queens.end(); iter++) {
//			if (iter->first == i || (iter->first - i == depth - iter->second || i - iter->first == depth - iter->second)){
//				isCollision = true;
//				break;
//			}
//		}
//
//		if (!isCollision) {
//			queens.push_back(make_pair(i, depth));
//			cnt += getQueenCaseCnt(depth + 1, queens, n);
//			queens.pop_back();
//		}
//	}
//
//	return  cnt;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N;
//	cin >> N;
//
//	vector<pair<int, int>> queens;
//	cout << getQueenCaseCnt(0, queens, N);
//
//	return 0;
//}