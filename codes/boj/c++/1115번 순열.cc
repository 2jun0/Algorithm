#include <iostream>

using namespace std;

/**
 * 지문은 너무 복잡하다.
 * 사실 순열의 숫자들은 자신의 다음 행선지 번호 (index)를 가리키고 있는데,
 * 이 일종의 그래프가 하나의 순환으로 이루어지는지 확인하는 문제다.
 * 
 * B는 0부터 출발해 N번 움직이는 경로를 보여주고 있다.
 * 
 * 예컨데, 2 0 1은 0 -> 2 -> 1로 움직일 것이고,
 * 2 1 0은 0 -> 2 -> 0로 움직일 것이다.
 * 
 * 그 다음 부터 문제는 매우 단순해진다.
*/

int N;
int P[50];
int visited[50];

void dfs(int x) {
  if (!visited[x]) {
    visited[x] = true;
    dfs(P[x]);
  }
}

int main() {
  cin >> N;

  for (int i = 0; i < N; i++) {
    cin >> P[i];
  }

  // 원래, 0이 있는 곳부터 출발해야 하지만 순환그래프라 상관없다.
  int cycleCnt = 0;
  for (int i = 0; i < N; i++) {
    if (!visited[i]) {
      cycleCnt++;
      dfs(i);
    }
  }

  if (cycleCnt == 1) {
    cout << '0' << '\n';
  } else {
    cout << cycleCnt << '\n';
  }

  return 0;
}