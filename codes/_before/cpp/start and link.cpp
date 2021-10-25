//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
//
//#define MAX(x,y) (((x) < (y))?(y):(x))
//#define ABS(x) (((x) < 0)?-(x):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//int _getMinDiff(int** S, int n, int me, bool isStartTeam, vector<int>& startTeam, vector<int>& linkTeam, int startTeamAbility = 0, int linkTeamAbility = 0) {
//	vector<int>::iterator iter;
//
//	if (me == n) {
//		return ABS(startTeamAbility - linkTeamAbility);
//	}
//
//	if (isStartTeam) {
//		for (iter = startTeam.begin(); iter != startTeam.end(); iter++) {
//			startTeamAbility += S[me][*iter] + S[*iter][me];
//		}
//
//		startTeam.push_back(me);
//	}
//	else {
//		for (iter = linkTeam.begin(); iter != linkTeam.end(); iter++) {
//			linkTeamAbility += S[me][*iter] + S[*iter][me];
//		}
//
//		linkTeam.push_back(me);
//	}
//	
//	int result;
//	if (linkTeam.size() == n / 2) {
//		result = _getMinDiff(S, n, me + 1, true, startTeam, linkTeam, startTeamAbility, linkTeamAbility);
//	}
//	else if(startTeam.size() == n/2) {
//		result = _getMinDiff(S, n, me + 1, false, startTeam, linkTeam, startTeamAbility, linkTeamAbility);
//	}
//	else {
//		result = _getMinDiff(S, n, me + 1, true, startTeam, linkTeam, startTeamAbility, linkTeamAbility);
//
//		if (result > 0) {
//			result = min(
//				result,
//				_getMinDiff(S, n, me + 1, false, startTeam, linkTeam, startTeamAbility, linkTeamAbility)
//			);
//		}
//	}
//
//	if (isStartTeam) {
//		startTeam.pop_back();
//	}
//	else {
//		linkTeam.pop_back();
//	}
//
//	return result;
//}
//
//int getMinDiff(int** S, int n) {
//	vector<int> startTeam, linkTeam;
//
//	return min(
//		_getMinDiff(S, n, 0, true, startTeam, linkTeam),
//		_getMinDiff(S, n, 0, false, startTeam, linkTeam)
//	);
//}
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	int N;
//	cin >> N;
//	int** S = new int* [N];
//	int sum = 0;
//	
//
//	for (int i = 0; i < N; i++) {
//		S[i] = new int[N];
//		for (int j = 0; j < N; j++) {
//			cin >> S[i][j];
//			sum += S[i][j];
//		}
//	}
//
//	cout << getMinDiff(S, N);
//
//	return 0;
//}