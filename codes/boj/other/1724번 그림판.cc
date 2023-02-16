#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>

using namespace std;

enum DIR {
  UP,
  DOWN,
  LEFT,
  RIGHT
};
int N, M, T;
bool map[500][500][4];
bool visited[500][500];

int dy[] = {-1, 1, 0, 0};
int dx[] = {0, 0, -1, 1};

void mapLine(int sx, int sy, int ex, int ey) {
  if (sx == ex) {
    // 세로
    for (int y = min(sy, ey); y < max(sy, ey); y++) {
      if (0 <= sx-1 && sx-1 < M) {
        // 왼쪽 칸
        map[y][sx-1][RIGHT] = false;
      }

      if (0 <= sx && sx < M) {
        // 오른쪽 칸
        map[y][sx][LEFT] = false;
      }
    }
  }
  else if (sy == ey) {
    // 가로
    for (int x = min(sx, ex); x < max(sx, ex); x++) {
      if (0 <= sy-1 && sy-1 < N) {
        // 위쪽 칸
        map[sy-1][x][DOWN] = false;
      }

      if (0 <= sy && sy < N) {
        // 오른쪽 칸
        map[sy][x][UP] = false;
      }
    }
  }
}

int bfs(int sy, int sx) {
  queue<pair<int, int> > q;

  visited[sy][sx] = true;
  q.push(make_pair(sy, sx));

  int cnt = 1;

  while (!q.empty()) {
    pair<int, int> p = q.front();
    q.pop();

    for (int i = 0; i < 4; i++) {
      if (!map[p.first][p.second][i]) {
        continue;
      }

      int ny = p.first + dy[i];
      int nx = p.second + dx[i];
      if (0<=ny && ny<N && 0<=nx && nx<M && !visited[ny][nx]) {
        visited[ny][nx] = true;
        cnt++;
        q.push(make_pair(ny, nx));
      }
    }
  }

  return cnt;
}

int main() {
  memset(map, true, sizeof(map));
  memset(visited, false, sizeof(visited));

  cin >> N >> M;
  cin >> T;

  for (int i = 0; i < T; i++) {
    int sx, sy, ex, ey;
    cin >> sy >> sx >> ey >> ex;

    mapLine(sx, sy, ex, ey);
  }

  int minCnt = N*M;
  int maxCnt = 0;

  for (int y = 0; y < N; y ++) {
    for (int x = 0; x < M; x ++) {
      if (!visited[y][x]) {
        int rs = bfs(y, x);
        minCnt = min(minCnt, rs);
        maxCnt = max(maxCnt, rs);
      }
    }
  }
  cout << maxCnt << '\n';
  cout << minCnt << '\n';

  return 0;
}