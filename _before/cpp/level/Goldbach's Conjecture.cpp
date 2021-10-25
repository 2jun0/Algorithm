//#include <iostream>
//#include <string.h>
//
//using namespace std;
//
//int main() {
//	int T, n;
//
//	cin >> T;
//
//	bool* isPrimeNum = new bool[10000];
//	memset(isPrimeNum, true, sizeof(bool) * 10000);
//
//	isPrimeNum[0] = false;
//
//	for (int num = 2; num <= 10000; num++) {
//		if (isPrimeNum[num - 1]) {
//			for (long long i = (long long)num * num; i <= 10000; i += num) {
//				isPrimeNum[i - 1] = false;
//			}
//		}
//	}
//
//	for (int i = 0; i < T; i++) {
//		cin >> n;
//		for (int j = n / 2; j >= 2; j--) {
//			if (isPrimeNum[j-1] && isPrimeNum[n - j - 1]) {
//				printf("%d %d\n", j, n - j);
//				break;
//			}
//		}
//	}
//
//	return 0;
//}