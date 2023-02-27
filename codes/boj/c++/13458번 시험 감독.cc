#include <iostream>

using namespace std;

int N, B, C;
int A[1000001];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  cin >> B >> C;

  long long rs = 0;
  for (int i = 0; i < N; i++) {
    int remain = A[i];

    remain -= B;
    rs++;

    if (remain > 0) {
      if (remain % C == 0) {
        rs += remain / C;
      } else {
        rs += remain / C + 1; 
      }
    }
  }

  cout << rs << '\n';

  return 0;
}