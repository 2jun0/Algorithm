//#include <iostream>
//#include <string>
//#include <cmath>
//#include <algorithm>
//
//#define MIN(x,y) ((x > y)?(y):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//int main() {
//	int N;
//	string str;
//	int sum;
//	int result = 0;
//
//	cin >> N;
//
//	for (int i = 1; i < N; i++) {
//		sum = i;
//
//		str = to_string(i);
//		for (int j = 0; j < str.size(); j++) {
//			sum += (str[j] - '0');
//		}
//
//		if (sum == N) {
//			result = i;
//			break;
//		}
//	}
//
//	cout << result;
//
//	return 0;
//}