//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
//#include <set>
//#include <queue>
//
//#define ABS(x) (((x) < 0)?-(x):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int N;
//	cin >> N;
//
//	vector<int> s;
//	vector<int>::iterator iter;
//
//	s.push_back(N);
//
//	int top, temp2;
//	int sum;
//
//	while (true) {
//		sum = 0;
//		top = s.back();
//		s.pop_back();
//
//		while (top == 1 && !s.empty()) {
//			sum++;
//
//			top = s.back();
//			s.pop_back();
//		}
//
//		if (top == 1) {
//			break;
//		}
//
//		s.push_back(top - 1);
//		top = s.back();
//
//		sum++;
//		while (top < sum) {
//			s.push_back(top);
//			sum -= top;
//		}
//
//		if (sum) s.push_back(sum);
//
//		for (iter = s.begin(); iter != s.end(); iter++) {
//			cout << *iter << ' ';
//		}
//		cout << '\n';
//	}
//
//	return 0;
//}