//#include <iostream>
//#include <string.h>
//
//using namespace std;
//
//int main() {
//	int n;
//
//	bool* isPrimeNum = new bool[246912];
//	int primeNumCnt[246912];
//	memset(isPrimeNum, true, sizeof(bool) * 246912);
//
//	isPrimeNum[0] = false;
//	primeNumCnt[0] = 0;
//
//	for (int num = 2; num <= 246912; num++) {
//		if (isPrimeNum[num - 1]) {
//			primeNumCnt[num - 1] = primeNumCnt[num - 2] + 1;
//
//			for (long long i = (long long)num * num; i <= 246912; i += num) {
//				isPrimeNum[i - 1] = false;
//			}
//		}
//		else {
//			primeNumCnt[num - 1] = primeNumCnt[num - 2];
//		}
//	}
//
//	cin >> n;
//	while (n > 0) {
//		cout << primeNumCnt[2 * n -1] - primeNumCnt[n - 1] << '\n';
//		cin >> n;
//	}
//
//	return 0;
//}