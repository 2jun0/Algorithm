//#include <iostream>
//#include <string.h>
//#include <cmath>
//
//#define MIN(x,y) ((x > y)?(y):(x))
//
//using namespace std;
//
//bool isRight(int a, int b, int c) {
//#define CHK(a,b,c) (pow(a,2) == pow(b,2) + pow(c,2))
//
//	if (a > b) {
//		if (a > c) {
//			// a
//			return CHK(a, b, c);
//		}
//		else {
//			// c
//			return CHK(c, b, a);
//		}
//	}
//	else if (b > a) {
//		if (b > c) {
//			// b
//			return CHK(b, a, c);
//		}
//		else {
//			// c
//			return CHK(c, b, a);
//		}
//	}
//}
//
//int main() {
//	int a, b, c;
//
//	cin >> a >> b >> c;
//	while (a + b + c) {
//		if (isRight(a, b, c)) {
//			cout << "right\n";
//		}
//		else {
//			cout << "wrong\n";
//		}
//
//		cin >> a >> b >> c;
//	}
//
//	return 0;
//}