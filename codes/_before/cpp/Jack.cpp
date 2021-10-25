//#include <iostream>
//#include <string.h>
//#include <cmath>
//#include <algorithm>
//
//#define MIN(x,y) ((x > y)?(y):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//int main() {
//	int N, M;
//	int sumOfThree = 0;
//	int sum;
//
//	cin >> N >> M;
//	int* cards = new int[N];
//
//	for (int i = 0; i < N; i++) {
//		cin >> cards[i];
//	}
//
//	//sort(cards, cards + N);
//
//	for (int i = 0; i < N-2; i++) {
//		for (int j = i + 1; j < N - 1; j++) {
//			for (int k = j + 1; k < N; k++) {
//				sum = cards[i] + cards[j] + cards[k];
//
//				if (M >= sum && sum > sumOfThree) {
//					sumOfThree = sum;
//				}
//			}
//		}
//		
//		
//	}
//
//	cout << sumOfThree;
//
//	return 0;
//}