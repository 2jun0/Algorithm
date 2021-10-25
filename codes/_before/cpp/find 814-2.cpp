//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
//#include <set>
//#include <cstdlib>
//
//#define ABS(x) (((x) < 0)?-(x):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//#define MUTATION_RATE 30 //max 100
//#define CNT 100
//#define ROW 14
//#define COL 8
//
//template<typename T>
//bool _defaultCmp(T& a, T& b) { return a <= b; }
//template<typename T, typename U>
//void mergeSortWith(T* arr, U* arr2, int start, int end, bool isAscending = true, bool (*cmp)(T&, T&) = _defaultCmp) {
//	int mid = (start + end) / 2;
//	T* sorted; U* sorted2;
//	int s = 0, i = start, j = mid + 1;
//
//	if (start < end) {
//		mergeSortWith(arr, arr2, start, mid, isAscending, cmp);
//		mergeSortWith(arr, arr2, mid + 1, end, isAscending, cmp);
//		sorted = new T[end - start + 1]; sorted2 = new U[end - start + 1];
//
//		while (i <= mid && j <= end) {
//			if (cmp(arr[i], arr[j]) == isAscending) {
//				sorted[s] = arr[i]; sorted2[s++] = arr2[i++];
//			}
//			else {
//				sorted[s] = arr[j]; sorted2[s++] = arr2[j++];
//			}
//		}
//
//		while (i <= mid) { sorted[s] = arr[i]; sorted2[s++] = arr2[i++]; }
//		while (j <= end) { sorted[s] = arr[j]; sorted2[s++] = arr2[j++]; }
//
//		for (int k = 0; k <= end - start; k++) {
//			arr[k + start] = sorted[k]; arr2[k + start] = sorted2[k];
//		}
//
//		delete[] sorted;
//	}
//}
//
//void random(int** board) {
//	for (int i = 0; i < COL; i++) {
//		for (int k = 0; k < ROW; k++) {
//			board[i][k] = rand() % 10;
//		}
//	}
//}
//
//// 2개의 board를 가지고 서로 조합함
//void nextGeneration(int*** board) {
//	int** ptr1, ** ptr2;
//
//	for (int b = 2; b < CNT; b++) {
//		if (rand() % 2 == 0) {
//			ptr1 = board[0];
//			ptr2 = board[1];
//		}
//		else {
//			ptr1 = board[1];
//			ptr2 = board[0];
//		}
//
//		if (rand() % 100 < MUTATION_RATE) {
//			random(board[b]);
//			continue;
//		}
//
//		int rowPin;
//		int colPin;
//		switch (rand() % 2) {
//		case 0:
//			rowPin = rand() % ROW;
//			for (int i = 0; i < COL; i++) {
//				for (int k = 0; k < rowPin; k++) {
//					board[b][i][k] = ptr1[i][k];
//				}
//				for (int k = rowPin; k < ROW; k++) {
//					board[b][i][k] = ptr2[i][k];
//				}
//			}
//			break;
//		case 1:
//			colPin = rand() % COL;
//			for (int k = 0; k < ROW; k++) {
//				for (int i = 0; i < colPin; i++) {
//					board[b][i][k] = ptr1[i][k];
//				}
//				for (int i = colPin; i < COL; i++) {
//					board[b][i][k] = ptr2[i][k];
//				}
//			}
//			break;
//		}
//
//	}
//}
//
//int getScore(int** board, bool mutatable = true) {
//	vector<vector<pair<int, int>>> num_poses;
//	num_poses.resize(10);
//
//	// 처음 0 부터 9까지 입력
//	for (int i = 0; i < COL; i++) {
//		for (int k = 0; k < ROW; k++) {
//			num_poses[board[i][k]].push_back(make_pair(i, k));
//		}
//	}
//
//	vector<pair<int, int>>::iterator iter;
//	pair<int, int> mask[] = {
//		make_pair(-1,-1),
//		make_pair(-1,0),
//		make_pair(-1,1),
//		make_pair(0,-1),
//		make_pair(0,1),
//		make_pair(1,-1),
//		make_pair(1,0),
//		make_pair(1,1)
//	};
//
//	int num = 10;
//	while (true) {
//		int a = num / 10;
//		int b = num % 10;
//		bool flag = false;
//
//		num_poses.resize(num_poses.size() + 1);
//
//		for (iter = num_poses[a].begin(); iter != num_poses[a].end(); iter++) {
//			for (pair<int, int> ip : mask) {
//				int i = ip.first + iter->first;
//				int k = ip.second + iter->second;
//
//				if ((i >= 0 && i < COL) && (k >= 0 && k < ROW)) {
//					if (board[i][k] == b) {
//						flag = true;
//						num_poses[num].push_back(make_pair(i, k));
//					}
//				}
//			}
//		}
//
//		if (!flag) {
//			if (mutatable) {
//				for (iter = num_poses[a].begin(); iter != num_poses[a].end(); iter++) {
//					for (pair<int, int> ip : mask) {
//						int i = ip.first + iter->first;
//						int k = ip.second + iter->second;
//
//						if ((i >= 0 && i < COL) && (k >= 0 && k < ROW)) {
//							if (rand() % 100 < MUTATION_RATE) {
//								board[i][k] = rand() % 10;
//							}
//						}
//					}
//				}
//			}
//
//			break;
//		}
//
//		num ++;
//	}
//
//	return num-1;
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	srand(1);
//
//	int*** boards = new int**[CNT];
//	for (int i = 0; i < CNT; i++) {
//		boards[i] = new int*[COL];
//		for (int k = 0; k < COL; k++) {
//			boards[i][k] = new int[ROW];
//		}
//	}
//
//	for (int i = 0; i < CNT; i++) {
//		random(boards[i]);
//	}
//
//	int scoreOfBoards[CNT];
//	for (int t = 0; t < 2; t++) {
//		scoreOfBoards[0] = getScore(boards[0], false);
//		scoreOfBoards[1] = getScore(boards[1], false);
//		for (int i = 2; i < CNT; i++) {
//			scoreOfBoards[i] = getScore(boards[i]);
//		}
//
//		mergeSortWith(scoreOfBoards, boards, 0, CNT - 1, false);
//
//		cout << scoreOfBoards[0] << '\n';
//
//		nextGeneration(boards);
//	}
//
//	cout << "Last Text\n";
//	for (int k = 0; k < COL; k++) {
//		for (int u = 0; u < ROW; u++) {
//			cout << boards[0][k][u];
//		}
//		cout << '\n';
//	}
//
//	return 0;
//}