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
//	int N;
//	cin >> N;
//
//	set<int> nums;
//	set<int> nums2;
//	nums.insert(N);
//
//	bool endFlag = false;
//
//	set<int>* ptr1;
//	set<int>* ptr2;
//
//	for (int i = 0; !endFlag; i++) {
//		if (i % 2 == 0) {
//			ptr1 = &nums;
//			ptr2 = &nums2;
//		}
//		else {
//			ptr1 = &nums2;
//			ptr2 = &nums;
//		}
//
//		for (set<int>::iterator iter = ptr1->begin(); iter != ptr1->end(); iter++) {
//			if ((*iter) == 1) {
//				endFlag = true;
//				cout << i;
//				break;
//			}
//
//			if ((*iter) % 3 == 0) {
//				ptr2->insert((*iter) / 3);
//			}
//			else {
//				ptr2->insert((*iter) - 1);
//			}
//
//			if ((*iter) % 2 == 0) {
//				ptr2->insert((*iter) / 2);
//			}
//			else {
//				ptr2->insert((*iter) - 1);
//			}
//		}
//
//		ptr1->clear();
//	}
//
//	return 0;
//}