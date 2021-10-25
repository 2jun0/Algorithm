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
//	long long numCnt[10];
//	long long numCnt2[10];
//
//	long long* ptr1;
//	long long* ptr2;
//
//	// init : level 0
//	numCnt[0] = 0;
//	for(int i = 1; i < 10; i++) {
//		numCnt[i] = 1;
//	}
//
//	for (int i = 1; i < n; i++) {
//		if (i % 2 == 0) {
//			ptr1 = numCnt2;
//			ptr2 = numCnt;
//		}
//		else {
//			ptr1 = numCnt;
//			ptr2 = numCnt2;
//		}
//
//		memset(ptr2, 0L, sizeof(long long) * 10);
//
//		ptr2[1] = (ptr2[1] + ptr1[0]) % 1000000000L;
//		for (int k = 1; k <= 8; k++)
//		{
//			ptr2[k - 1] = (ptr2[k - 1] + ptr1[k]) % 1000000000L;
//			ptr2[k + 1] = (ptr2[k + 1] + ptr1[k]) % 1000000000L;
//		}
//		ptr2[8] = (ptr2[8] + ptr1[9]) % 1000000000L;
//	}
//
//	if (n % 2 == 0) {
//		ptr1 = numCnt2;
//	}
//	else {
//		ptr1 = numCnt;
//	}
//
//	long long cnt = 0;
//	for (int i = 0; i < 10; i++) {
//		cnt += ptr1[i];
//	}
//	cout << cnt % 1000000000L;
//
//	return 0;
//}