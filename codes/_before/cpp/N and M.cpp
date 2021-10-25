//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//
//#define MIN(x,y) ((x > y)?(y):(x))
//#define MAX(x,y) ((x < y)?(y):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//void getNum(int* nums, int m, int M, int N) {
//	bool flag = true;
//
//	if (m == M) {
//		for (int i = 0; i < m; i++) {
//			cout << nums[i] + 1<< ' ';
//		}
//		cout << '\n';
//	}
//	else {
//		for (int num = (m > 0 ? nums[m-1] : 0); num < N; num++) {
//			flag = true;
//			/*for (int j = 0; j < m; j++) {
//				if (nums[j] == num) {
//					flag = false;
//					break;
//				}
//			}*/
//
//			if (flag) {
//				nums[m] = num;
//				getNum(nums, m + 1, M, N);
//			}
//		}
//	}
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N, M;
//	cin >> N >> M;
//
//	int* nums = new int[M];
//
//	getNum(nums, 0, M, N);
//
//	return 0;
//}