//#include <iostream>
//#include <string.h>
//
//using namespace std;
//
//int main() {
//	int M, N;
//	cin >> M >> N;
//
//	bool* isPrimeNum = new bool[N];
//	memset(isPrimeNum, true, sizeof(bool) * N);
//
//	isPrimeNum[0] = false;
//	for (int num = 2; num <= N; num++) {
//		if (isPrimeNum[num - 1]) {
//			if (num >= M) {
//				cout << num << '\n';
//			}
//
//			for (long long i = (long long)num*num; i <= N; i += num) {
//				isPrimeNum[i-1] = false;
//			}
//		}
//	}
//
//	return 0;
//}