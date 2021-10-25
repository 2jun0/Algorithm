//#include <iostream>
//
//using namespace std;
//
//int main() {
//	int M, N;
//	int min = 0, sum = 0;
//	bool flag;
//
//	cin >> M;
//	cin >> N;
//
//	for (int num = M; num <= N; num++) {
//		if (num == 1) {
//			flag = false;
//		}
//		else {
//			flag = true;
//
//			for (int i = 2; i < num; i++) {
//				if (num % i == 0) {
//					flag = false;
//					break;
//				}
//			}
//		}
//
//		if (flag) {
//			if (!min) {
//				min = num;
//			}
//
//			sum += num;
//		}
//	}
//
//	if (sum == 0) {
//		cout << -1;
//	}
//	else {
//		cout << sum << endl << min;
//	}
//
//	return 0;
//}