#include <iostream>
using namespace std;

int main2() {
	int x;
	cin >> x;

	int l_i = 1;
	int l_c = 1;
	int l_x = 1;
	int x_i;

	while(true)  {
		if (x < l_x) {
			l_i--;
			l_c--;
			l_x -= l_c;
			x_i = (l_i % 2 == 0) ? x - l_x + 1 : l_c - (x - l_x);
			break;
		}
		l_i++;
		l_x += l_c;
		l_c++;
	}

	cout << x_i << '/' << (l_c - x_i + 1);
	return 0;
}