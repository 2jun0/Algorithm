//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
//#include <set>
//
//#define ABS(x) (((x) < 0)?-(x):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//int getLCSLength(string& A, string& B) {
//	int* lcs = new int[B.length()];
//	memset(lcs, 0, sizeof(int) * B.length());
//
//	int* prevLcs = new int[B.length()]; // 이전의 lcs 정보
//	for (int a = 0; a < A.length(); a++) {
//		memcpy(prevLcs, lcs, sizeof(int) * B.length()); // 복★사
//
//		for (int b = 0; b < B.length(); b++) {
//			if (A[a] == B[b]) {
//				// 새로 기입할 숫자
//				int num = prevLcs[b-1] + 1;
//
//				for (int i = b; i < B.length() && lcs[i] < num; i++) { // 뒤의 작은 숫자들을 동기화 한다.
//					lcs[i] = num;
//				}
//			}
//		}
//	}
//
//	int lcsLen = lcs[B.length()-1];
//	delete[] lcs;
//	delete[] prevLcs;
//
//	return lcsLen;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	string A;
//	string B;
//
//	cin >> A;
//	cin >> B;
//
//	cout << getLCSLength(A, B);
//
//	return 0;
//}