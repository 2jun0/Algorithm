//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
//#include <set>
//
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
//	if (n == 1) {
//		int temp;
//		cin >> temp;
//		cout << temp;
//	}
//	else {
//		// 0: original value
//		// 1: 1step or case of jump from back stair
//		// 2: 2step
//		int** wine = new int*[n];
//
//		for (int i = 0; i < n; i++) {
//			wine[i] = new int[3];
//			cin >> wine[i][0];
//		}
//
//		wine[0][1] = wine[0][0];
//		wine[1][1] = wine[1][0];
//		wine[1][2] = wine[1][0] + wine[0][1];
//		int maxWineWithoutLastest = wine[0][0];
//		int maxWine = max(maxWineWithoutLastest, wine[1][2]);
//
//		for (int i = 2; i < n; i++) {
//			wine[i][1] = wine[i][0] + maxWineWithoutLastest;
//			wine[i][2] = wine[i][0] + wine[i - 1][1];
//
//			maxWineWithoutLastest = max(max(wine[i - 1][1], wine[i - 1][2]), maxWineWithoutLastest);
//			maxWine = max(max(wine[i][1], wine[i][2]), maxWine);
//		}
//
//		//	06 06 06
//		//	10 10 16
//		//	13 18 23
//		//	09 25 27
//		//	08 31 33
//		//	01 28 
//
//		cout << maxWine;
//	}
//
//	return 0;
//}