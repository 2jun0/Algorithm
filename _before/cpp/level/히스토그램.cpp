//#include <iostream>
//#include<cstring>
//#include <string>
//#include <cmath>
//#include <algorithm>
//#include <stack>
//#include <vector>
//#include <set>
//#include <queue>
//#include <map>
//
//#define ABS(x) (((x) < 0)?-(x):(x))
//#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
//#define PI 3.1415926535897932384
//
//using namespace std;
//
//int main() {
//	ios_base::sync_with_stdio(false);
//	cin.tie(0);
//
//
//	int N;
//	cin >> N;
//
//	int* nums = new int[N+2];
//	nums[0] = -1; nums[N + 1] = -1;
//	for (int i = 1; i <= N; i++) {
//		cin >> nums[i];
//	}
//	stack<int> s;
//
//	int rect = 0;
//	s.push(0);
//	for(int k = 1; k <= N+1; k++) {
//		while (nums[s.top()] > nums[k]) {
//			int height = nums[s.top()];
//			s.pop();
//			int width = k - s.top() - 1;
//			rect = max(rect, height * width);
//		}
//		s.push(k);
//	} 
//
//	delete[] nums;
//	cout << rect;
//
//	return 0;
//}