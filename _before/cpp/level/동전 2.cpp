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
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//	int n, k;
//	cin >> n >> k;
//
//	int* coins = new int[n+1];
//	for (int i = 1; i <= n; i++)	{
//		cin >> coins[i];
//	}
//
//	int* cnts = new int[k + 1];
//	cnts[0] = 0;
//	for (int i = 1; i <= k; i++) {
//		cnts[i] = 1000001;
//	}
//	for (int i = 1; i <= n; i++) {
//		for (int j = 0; j <= k - coins[i]; j++) {
//			cnts[coins[i] + j] = min(cnts[coins[i] + j], cnts[j] + 1);
//		}
//	}
//
//	cout << ((cnts[k] == 1000001) ? -1 : cnts[k]);
//
//	delete[] cnts;
//	delete[] coins;
//
//	return 0;
//}