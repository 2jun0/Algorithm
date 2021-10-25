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
//const int MINUS = 1<<0;
//const int ZERO = 1<<1;
//const int PLUS = 1<<2;
//
//int getPaperCnt(int** paper, int startX, int endX, int startY, int endY, int* cnts) {
//	if (startX == endX && startY == endY) {
//		switch (paper[startX][startY]) {
//		case -1:
//			cnts[0]+=1;
//			return MINUS;
//		case 0:
//			cnts[1]+=1;
//			return ZERO;
//		case 1:
//			cnts[2]+=1;
//			return PLUS;
//		}
//	}
//
//	int increX = (endX - startX + 1) / 3;
//	int increY = (endY - startY + 1) / 3;
//
//	int flag = getPaperCnt(paper, startX, endX-2*increX, startY, endY-2*increY, cnts);
//	flag |= getPaperCnt(paper, startX, endX-2*increX, startY + increY, endY-increY, cnts);
//	flag |= getPaperCnt(paper, startX, endX-2*increX, startY + 2 * increY, endY, cnts);
//	flag |= getPaperCnt(paper, startX + increX, endX-increX, startY, endY-2*increY, cnts);
//	flag |= getPaperCnt(paper, startX + increX, endX-increX, startY + increY, endY-increY, cnts);
//	flag |= getPaperCnt(paper, startX + increX, endX-increX, startY + 2 * increY, endY, cnts);
//	flag |= getPaperCnt(paper, startX + 2*increX, endX, startY, endY-2*increY, cnts);
//	flag |= getPaperCnt(paper, startX + 2*increX, endX, startY + increY, endY-increY, cnts);
//	flag |= getPaperCnt(paper, startX + 2*increX, endX, startY + 2 * increY, endY, cnts);
//
//	switch (flag)
//	{
//	case MINUS:
//		cnts[0] -= 8;
//		return MINUS;
//	case ZERO:
//		cnts[1] -= 8;
//		return ZERO;
//	case PLUS:
//		cnts[2] -= 8;
//		return PLUS;
//	default:
//		return flag;
//	}
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int n;
//	cin >> n;
//
//	int** paper = new int*[n];
//	for (int i = 0; i < n; i++) {
//		paper[i] = new int[n];
//		for (int k = 0; k < n; k++) {
//			cin >> paper[i][k];
//		}
//	}
//
//	int cnt[3];
//	cnt[0] = cnt[1] = cnt[2] = 0;
//
//	getPaperCnt(paper, 0, n - 1, 0, n - 1, cnt);
//
//	for(int i = 0; i < 3; i++) cout << cnt[i] << '\n';
//
//	for (int i = 0; i < n; i++) delete[] paper[i];
//	delete[] paper;
//
//	return 0;
//}