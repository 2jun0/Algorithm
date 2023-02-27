#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
int A[50];
bool visited[50];
int B[50];

bool canUse(int a) {
  bool havePositive = false; // a, a + 1이 아닌 것이 있는지 궁금
  bool haveNegative = false; // a + 1이 있는지 궁금

  for (int other = 0; other < N; other++) {
    if (visited[other]) continue;

    if (A[other] == a+1) haveNegative = true;
    else if (A[other] != a) havePositive = true;
  }

  return !(haveNegative && !havePositive);
}

bool dfs(int ai, int bi) {
  visited[ai] = true;
  B[bi] = A[ai];

  bool flag = false;

  if (bi == N-1) {
    flag = true;
  } else {
    for (int nxtAi = 0; nxtAi < N; nxtAi++) {
      if (!visited[nxtAi] && B[bi] + 1 != A[nxtAi] && canUse(A[nxtAi])) {
        if (dfs(nxtAi, bi+1)) {
          flag = true;
          break;
        }
      }
    }
  }

  visited[ai] = false;
  return flag;
}

int main() {
  cin >> N;
  
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  sort(A, A+N);

  for (int i = 0; i < N; i++) {
    if (canUse(A[i]) && dfs(i, 0)) {
      break;
    }
  }

  for (int i = 0; i < N; i++) {
    cout << B[i] << ' ';
  }
  cout << '\n';

  return 0;
}