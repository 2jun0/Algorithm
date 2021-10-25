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
//class Record {
//public:
//	int n;
//	int* nums_cnt;
//
//	Record(int _n) {
//		n = _n;
//		nums_cnt = new int[n];
//		memset(nums_cnt, 0, sizeof(int) * n);
//	}
//
//	Record(int _n, int* _nums_cnt) {
//		n = _n;
//		nums_cnt = new int[n];
//		memcpy(nums_cnt, _nums_cnt, sizeof(int)*n);
//	}
//
//	~Record() {
//		delete[] nums_cnt;
//	}
//
//	Record *clone(int next) {
//		Record* record = new Record(n, nums_cnt);
//		record->nums_cnt[next] ++;
//
//		return record;
//	}
//};
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N;
//	cin >> N;
//
//	int num;
//
//	int* nums_cnt = new int[N];
//	memset(nums_cnt, 0, sizeof(int) * N);
//
//	for (int i = 0; i < N * 2 - 1; i++) {
//		cin >> num;
//		nums_cnt[num]++;
//	}
//
//	vector<Record*>** memo = new vector<Record*>*[N]; // [개수][나머지]
//	for (int i = 0; i < N; i++) {
//		memo[i] = new vector<Record*>[N+1];
//	}
//	for (int k = 0; k < N; k++) {
//		memo[0][k] = new vector<Record*>[N + 1];
//	}
//
//	for(int cnt = )
//
//	return 0;
//}