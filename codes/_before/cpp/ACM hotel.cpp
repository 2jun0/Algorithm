//#include <iostream>
//
//using namespace std;
//
//int main() {
//	int T, H, W, N;
//	int num, floor;
//	cin >> T;
//
//	for (int i = 0; i < T; i++) {
//		cin >> H >> W >> N;
//
//		// 호수 : (N-1) / H + 1
//		num = (N - 1) / H + 1;
//		// 충수 : (N-1) % H + 1
//		floor = (N - 1) % H + 1;
//
//		printf("%d%02d\n", floor, num);
//	}
//
//	return 0;
//}