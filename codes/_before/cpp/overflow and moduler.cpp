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
//	int N, M;
//	cin >> N >> M;
//
//	long long result, temp;
//	cin >> result;
//	result %= M;
//	for (int i = 1; i < N; i++) {
//		cin >> temp;
//		result *= (temp % M);
//		result %= M;
//	}
//
//	cout << result;
//
//	return 0;
//}