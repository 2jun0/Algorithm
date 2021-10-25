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
//	string str;
//	cin >> str;
//	string bomb;
//	cin >> bomb;
//	int bn = bomb.length();
//
//	string result;
//	result.assign(str.size(), 0);
//	int k = 0;
//	for (int i = 0; i <= str.length(); i++) {
//		if (k >= bn && result.compare(k - bn, bn, bomb) == 0)
//			k -= bn;
//		result[k++] = str[i];
//	}
//	result[k-1] = 0;
//	if(k-1) cout << result.c_str();
//	else cout << "FRULA";
//
//	return 0;
//}