#include <iostream>
#include<cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <stack>
#include <vector>
#include <set>
#include <queue>
#include <map>

#define ABS(x) (((x) < 0)?-(x):(x))
#define SWAP(a,b, temp) temp = (a); a = (b); b = temp;
#define PI 3.1415926535897932384

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int s_cnt, p_cnt;
	cin >> s_cnt >> p_cnt;

	int sum = 0;
	int cut_cnt = 0;
	int cell_size = p_cnt;
	while (cell_size < s_cnt) {
		cell_size += p_cnt;
	}
	int cell_sum = cell_size;
	while (sum < s_cnt * p_cnt) {
		sum += s_cnt;
		if (sum == cell_sum) {
			cell_sum += cell_size;
		}
		else if (sum > cell_sum) {
			cell_sum += cell_size;
			cut_cnt++;
		}
		else {
			cut_cnt++;
		}
	}

	if (sum != cell_sum-cell_size) {
		cut_cnt--;
	}

	cout << cut_cnt;

	return 0;
}