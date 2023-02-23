#include <iostream>
#include <numeric>
using namespace std;

int N;
int dp[16];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  dp[0] = 0;

  cin >> N;
  for (int i = 0; i < N; i++) {
    if (i > 0)
      dp[i] = max(dp[i-1], dp[i]);

    int T, P;
    cin >> T >> P;

    if (i+T <= N)
      dp[i+T] = max(dp[i+T], dp[i]+P);
  }

  dp[N] = max(dp[N-1], dp[N]);

  cout << dp[N] << '\n';

  return 0;
}