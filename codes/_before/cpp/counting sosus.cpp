//#include <iostream>
//
//using namespace std;
//
//bool isPrimeNum(int& num) {
//	if (num == 1) return false;
//
//	for (int i = 2; i < num; i++) {
//		if (num % i == 0) {
//			return false;
//		}
//	}
//
//	return true;
//}
//
//int main() {
//	int N, a, cnt = 0;
//
//	cin >> N;
//
//	for (int i = 0; i < N; i++) {
//		cin >> a;
//		
//		if (isPrimeNum(a)) {
//			cnt++;
//		}
//	}
//
//	cout << cnt << endl;
//
//	return 0;
//}