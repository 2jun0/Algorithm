//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
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
//		int** upstairs = new int*[n];
//
//		for (int i = 0; i < n; i++) {
//			upstairs[i] = new int[3];
//			cin >> upstairs[i][0];
//		}
//
//		upstairs[0][1] = upstairs[0][0];
//		upstairs[1][1] = upstairs[1][0];
//		upstairs[1][2] = upstairs[1][0] + upstairs[0][1];
//
//		for (int i = 2; i < n; i++) {
//			upstairs[i][1] = upstairs[i][0] + max(upstairs[i - 2][2], upstairs[i - 2][1]);
//			upstairs[i][2] = upstairs[i][0] + upstairs[i - 1][1];
//		}
//
//		//	10 10 10
//		//	20	 20 30
//		//	15 25 35
//		//	25 55 50
//		//	10 35 65
//		//	20 75 55
//
//		cout << max(upstairs[n - 1][1], upstairs[n - 1][2]);
//	}
//
//	return 0;
//}