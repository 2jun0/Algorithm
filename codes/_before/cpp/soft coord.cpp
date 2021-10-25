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
//template<typename T>
//void mergeSort(T* arrX, T* arrY, int start, int end, bool isAscending = true) {
//	int mid = (start + end) / 2;
//	T* sortedX, *sortedY;
//	int s = 0;
//	int i = start, j = mid + 1;
//
//	if (start < end) {
//		mergeSort(arrX, arrY, start, mid, isAscending);
//		mergeSort(arrX, arrY, mid + 1, end, isAscending);
//
//		sortedX = new T[end - start + 1];
//		sortedY = new T[end - start + 1];
//
//		while (i <= mid && j <= end) {
//			if (isAscending) {
//				if (arrX[i] < arrX[j]) {
//					sortedX[s] = arrX[i];
//					sortedY[s] = arrY[i];
//					i++;
//				}
//				else if(arrX[i] == arrX[j]) {
//					if (arrY[i] < arrY[j]) {
//						sortedX[s] = arrX[i];
//						sortedY[s] = arrY[i];
//						i++;
//					}
//					else {
//						sortedX[s] = arrX[j];
//						sortedY[s] = arrY[j];
//						j++;
//					}
//				}else{
//					sortedX[s] = arrX[j];
//					sortedY[s] = arrY[j];
//					j++;
//				}
//				s++;
//			}
//			else {
//				if (arrX[i] > arrX[j]) {
//					sortedX[s] = arrX[i];
//					sortedY[s] = arrY[i];
//					i++;
//				}
//				else if (arrX[i] == arrX[j]) {
//					if (arrY[i] < arrY[j]) {
//						sortedX[s] = arrX[i];
//						sortedY[s] = arrY[i];
//						i++;
//					}
//					else {
//						sortedX[s] = arrX[j];
//						sortedY[s] = arrY[j];
//						j++;
//					}
//				}else {
//					sortedX[s] = arrX[j];
//					sortedY[s] = arrY[j];
//					j++;
//				}
//				s++;
//			}
//		}
//
//		while (i <= mid) {
//			sortedX[s] = arrX[i];
//			sortedY[s] = arrY[i];
//			i++;  s++;
//		}
//
//		while (j <= end) {
//			sortedX[s] = arrX[j];
//			sortedY[s] = arrY[j];
//			j++;  s++;
//		}
//
//		for (int k = 0; k <= end - start; k++) {
//			arrX[k + start] = sortedX[k];
//			arrY[k + start] = sortedY[k];
//		}
//
//		delete[] sortedX;
//		delete[] sortedY;
//	}
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N;
//	cin >> N;
//	int* arrX = new int[N];
//	int* arrY = new int[N];
//
//	for (int i = 0; i < N; i++) {
//		cin >> arrX[i] >> arrY[i];
//	}
//
//	mergeSort(arrY, arrX, 0, N-1);
//
//	for (int i = 0; i < N; i++) {
//		cout << arrX[i] << ' ' << arrY[i] << '\n';
//	}
//
//	return 0;
//}