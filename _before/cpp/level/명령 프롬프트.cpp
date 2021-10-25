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
//	int N;
//	cin >> N;
//	string* files = new string[N];
//	for (int i = 0; i < N; i++)	{
//		cin >> files[i];
//	}
//
//	string result = "";
//	for (int k = 0; k < files[0].size(); k++)	{
//		bool flag = true;
//		char c = files[0][k];
//		for (int i = 1; i < N; i++)	{
//			if (c != files[i][k]) {
//				flag = false;
//				break;
//			}
//		}
//
//		if (flag) {
//			result += c;
//		}
//		else {
//			result += '?';
//		}
//	}
//
//	cout << result;
//
//	delete[] files;
//	return 0;
//}