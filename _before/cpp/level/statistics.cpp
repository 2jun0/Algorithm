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
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N;
//	int num;
//	int mean, sum = 0;
//	int center; bool findCenter = false;
//	int mode_first_idx = -1, mode_second_idx = -1;
//	int max = -4000, min = 4000;
//	int cnt[8001];
//	memset(cnt, 0, sizeof(int) * 8001);
//
//	cin >> N;
//
//	for (int i = 0; i < N; i++) {
//		cin >> num;
//		sum += num;
//		cnt[num + 4000] ++;
//	}
//
//	mean = (int)round((double)sum / N);
//
//	for (int i = 0, c = 0, mid = N / 2 + 1; i < 8001; i++) {
//		if (cnt[i]) {
//			if (!findCenter) {
//				c += cnt[i];
//
//				if (c >= mid) {
//					center = i - 4000;
//					findCenter = true;
//				}
//			}
//
//			if (mode_first_idx == -1 || cnt[i] > cnt[mode_first_idx]) {
//				mode_first_idx = i;
//				mode_second_idx = -1;
//			}
//			else if(cnt[i] == cnt[mode_first_idx]) {
//				if (mode_second_idx == -1) {
//					mode_second_idx = i;
//				}
//			}
//
//			min = MIN(min, i - 4000);
//			max = MAX(max, i - 4000);
//		}
//	}
//
//	std::cout << mean << '\n';
//	std::cout << center << '\n';
//	std::cout << ((mode_second_idx != -1) ? (mode_second_idx - 4000) : (mode_first_idx - 4000)) << '\n';
//	std::cout << max - min;
//}