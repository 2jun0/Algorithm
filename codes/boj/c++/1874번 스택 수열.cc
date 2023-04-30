#include <iostream>
#include<cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <stack>
#include <vector>
#include <set>

#define ABS(x) (((x) < 0)?-(x):(x))
#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
#define PI 3.1415926535897932384

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);

	int n;
	cin >> n;

	stack<int> stk;
	
	int *nums = new int[n];
	string s = "";

	for (int i = 0; i < n; i++) {
		cin >> nums[i];
	}

	int num_idx = 0;
	for(int i = 1; i <= n; i++) {
		s+= "+\n";
		stk.push(i);

		while (!stk.empty() && stk.top() == nums[num_idx]) {
			s += "-\n";
			stk.pop();

			num_idx++;
		}
	}

	if (num_idx >= n - 1) {
		cout << s;
	}
	else {
		cout << "NO";
	}


	return 0;
}