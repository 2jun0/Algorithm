#include <iostream>
#include <numeric>
#include <string>
using namespace std;

/**
 * aaa bb c의 수가 있을때, (길이를 표시하기 위해 반복 표시함)
 * 모든 경우의 수 aaabbc, aaacbb, bbaaac, bbcaaa, caaabb, cbbaaa가 있다.
 * 이때 aaabbc % k는 아래와 같이 구할 수 있다.
 * 
 * ((a*10^3) + (b*10) + c) % k
 * aaa bb c는 "나머지 값" 과 "위치 10^n", "중복 불가"에 묶여있다.
 * 비트마스킹으로 중복감지를 표현할 수 있다. 
 * 위치값도 방문했던 숫자들의 크기 합을 구하면 구할 수 있다.
 * 고로 dp[visited mask][나머지 값]로 묶을 수 있다.
*/
#define BigInt string

int N;
BigInt A[15];
int mods[15];
int sizes[15];
int sizeSum = 0;
int K;
long long dp[1<<15][100];

int _powModCache[100];
int tenPowMod(int b) {
  if (_powModCache[b]) return _powModCache[b];

  if (b == 0) return _powModCache[b] = 1 % K;
  if (b == 1) return _powModCache[b] = 10 % K;

  return _powModCache[b] = (tenPowMod(b / 2) * tenPowMod(b - b / 2)) % K;
}

int getBigIntSize(BigInt& x) {
  return x.size();
}

int modBigInt(BigInt& x, int k) {
  int rs = 0;
  for (int i = 0; i < x.size(); i++) {
    int pos = x.size() - i - 1;
    int digit = x[i]-'0';
    rs = (rs + ((digit % k) * tenPowMod(pos)) % k) % k;
  }
  return rs;
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  cin >> N;

  for (int i = 0; i < N; i++) {
    cin >> A[i];
    sizes[i] = getBigIntSize(A[i]);
  }
  sizeSum = accumulate(sizes, sizes+N, 0);

  cin >> K;

  for (int i = 0; i < N; i++) {
    mods[i] = modBigInt(A[i], K);
  }

  dp[0][0] = 1;

  for (int bits = 0; bits < 1<<N; bits++) {
    for (int mod = 0; mod < K; mod++) {
      if (!dp[bits][mod]) continue; // 경우의 수가 없으면 방문 의미가 없다.

      for (int i = 0; i < N; i++) {
        if (bits & (1 << i)) continue; // 방문 체크

        int nxtBits = bits | 1 << i;
        int nxtMod = (mods[i] + tenPowMod(A[i].size()) * mod) % K;
        dp[nxtBits][nxtMod] += dp[bits][mod];
      }
    }
  }

  long long up = dp[(1<<N)-1][0];
  long long down = accumulate(dp[(1<<N)-1], dp[(1<<N)-1]+K, 0l);

  long long g = gcd(up, down);

  up /= g;
  down /= g;

  cout << up << '/' << down << '\n';

  return 0;
}