//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
//
//#define MAX(x,y) (((x) < (y))?(y):(x))
//#define ABS(x) (((x) < 0)?-(x):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int n;
//	cin >> n;
//
//	int** costs = new int*[n];
//
//	for (int i = 0; i < n; i++) {
//		costs[i] = new int[3];
//		cin >> costs[i][0] >> costs[i][1] >> costs[i][2];
//	}
//
//	for (int i = 1; i < n; i++) {
//		if (costs[i - 1][0] < costs[i - 1][1]) {
//			if (costs[i - 1][0] < costs[i - 1][2]) {
//				costs[i][1] += costs[i - 1][0];
//				costs[i][2] += costs[i - 1][0];
//
//				if (costs[i - 1][1] < costs[i - 1][2]) {
//					// 0 1 2
//					costs[i][0] += costs[i - 1][1];
//				}
//				else {
//					// 0 2 1
//					costs[i][0] += costs[i - 1][2];
//				}
//			}
//			else {
//				// 2 0 1
//				costs[i][0] += costs[i - 1][2];
//				costs[i][1] += costs[i - 1][2];
//				costs[i][2] += costs[i - 1][0];
//			}
//		}
//		else {
//			if (costs[i - 1][1] < costs[i - 1][2]) {
//				costs[i][0] += costs[i - 1][1];
//				costs[i][2] += costs[i - 1][1];
//
//				if (costs[i - 1][0] < costs[i - 1][2]) {
//					// 1 0 2
//					costs[i][1] += costs[i - 1][0];
//				}
//				else {
//					// 1 2 0
//					costs[i][1] += costs[i - 1][2];
//				}
//			}
//			else {
//				// 2 1 0
//				costs[i][0] += costs[i - 1][2];
//				costs[i][1] += costs[i - 1][2];
//				costs[i][2] += costs[i - 1][1];
//			}
//		}
//	}
//
//	cout << min(min(costs[n - 1][0], costs[n - 1][1]), costs[n - 1][2]);
//
//	return 0;
//}