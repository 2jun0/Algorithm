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
//	int N;
//	cin >> N;
//
//	int cntOf2 = 0;
//	int cntOf5 = 0;
//	for (int i = 2, num; i <= N; i ++) {
//		num = i;
//
//		while (num % 2 == 0) {
//			num /= 2;
//			cntOf2++;
//		}
//
//		while (num % 5 == 0) {
//			num /= 5;
//			cntOf5++;
//		}
//	}
//
//	cout << min(cntOf2, cntOf5);
//
//	return 0;
//}