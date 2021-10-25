//#include <iostream>
//
//using namespace std;
//
//void getNextFloorNums(int* floorNums, int n) {
//	for (int i = 1; i < n; i++) {
//		floorNums[i] += floorNums[i - 1];
//	 }
//}
//
//int main() {
//	int T, k, n;
//	cin >> T;
//
//	for (int i = 0; i < T; i++) {
//		cin >> k;
//		cin >> n;
//
//		int* floorNums = new int[n];
//		for (int j = 0; j < n; j++) {
//			floorNums[j] = j + 1;
//		}
//
//		for (int k_i = 0; k_i < k; k_i++) {
//			getNextFloorNums(floorNums ,n);
//		}
//		// 1 5 15 35
//		// 1 4 10 20
//		// 1 3 6 10 15  => 
//		// 1 2 3  4  5  6  7  8  9 => n
//
//		cout << floorNums[n - 1] << endl;
//	}
//
//	return 0;
//}