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
//int main() {
//	ios_base::sync_with_stdio(false);
//
//	int k;
//	cin >> k;
//
//	stack<int> s;
//	int temp;
//	for (int i = 0; i < k; i++) {
//		cin >> temp;
//
//		if (temp == 0) {
//			s.pop();
//		}
//		else {
//			s.push(temp);
//		}
//	}
//
//	int sum = 0;
//	while(!s.empty()) {
//		sum += s.top();
//		s.pop();
//	}
//
//	cout << sum;
//
//	return 0;
//}