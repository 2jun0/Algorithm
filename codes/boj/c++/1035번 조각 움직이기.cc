#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>

using namespace std;

struct Pos {
  int y;
  int x;
};

vector<Pos> A;
char map[5][5];
bool visited[5][5];

int dy[] = {0,0,-1,1};
int dx[] = {-1,1,0,0};

bool isConnected() {
  bool cvisited[5][5];
  memset(cvisited, false, sizeof(cvisited));

  queue<Pos> q;

  cvisited[A[0].y][A[0].x] = true;
  q.push(A[0]);

  int cnt = 0;

  while (!q.empty()) {
    Pos cur = q.front();
    q.pop();

    cnt ++;

    for (int i = 0; i < 4; i++) {
      Pos nxt = { dy[i] + cur.y, dx[i] + cur.x };

      if (0<=nxt.y&&nxt.y<5&&0<=nxt.x&&nxt.x<5&&!cvisited[nxt.y][nxt.x]&&visited[nxt.y][nxt.x]) {
        cvisited[nxt.y][nxt.x] = true;

        q.push(nxt);
      }
    }
  }

  return cnt == A.size();
}

int dfs(int i) {
  if (i >= A.size()) {
    return isConnected() ? 0 : 1000000000;
  }

  int minDiff = 1000000000;

  Pos prev = A[i];
  visited[A[i].y][A[i].x] = false;
  for (int y = 0; y < 5; y++) {
    for (int x = 0; x < 5; x++) {
      if (visited[y][x]) continue;

      visited[y][x] = true;
      A[i] = (Pos){ y, x };
      int diff = abs(prev.y - y) + abs(prev.x - x);
      int nxtDiff = dfs(i+1);

      minDiff = min(minDiff, diff+nxtDiff);

      A[i] = prev;
      visited[y][x] = false;
    }
  }
  A[i] = prev;
  visited[A[i].y][A[i].x] = true;

  return minDiff;
}

int main() {
  for (int y = 0; y < 5; y++) {
    cin >> map[y];
  }

  for (int y = 0; y < 5; y++) {
    for (int x = 0; x < 5; x++) {
      if (map[y][x] == '*') {
        A.push_back((Pos){y, x});
        visited[y][x] = true;
      }
    }
  }

  int rs = dfs(0);
  cout << rs << '\n';

  return 0;
}