#include <iostream>
#include <cstring>
#include <deque>
#include <numeric>
#include <set>
using namespace std;

#define DOOR '#'
#define WALL '*'
#define OPEN_DOOR 'P'
#define MAN '$'
#define EMPTY '.'
#define EXIT '0'

struct Pos {
  int y;
  int x;

  bool operator!=(Pos& pos) {
    return y != pos.y || x != pos.x;
  }
  bool operator<(const Pos& pos) const {
    return y < pos.y || x < pos.x;
  }
};

int T, h, w;
char map[102][102];

int dy[] = {0, 0, -1, 1};
int dx[] = {-1, 1, 0, 0};

int costs[3][102][102];
Pos rePath[3][102][102];

bool inRange(Pos x) {
  return 0<= x.y && x.y < h && 0<= x.x && x.x < w;
}

int meetEachOthers(Pos ps[], int cnt) {
  struct Entry {
    Pos pos;
    int offset; // ps의 idx
  };

  memset(costs, -1, sizeof(costs));
  deque<Entry> q;

  for (int offset = 0; offset < cnt; offset++) {
    Pos &p = ps[offset];

    rePath[offset][p.y][p.x] = p;
    costs[offset][p.y][p.x] = 0;
    q.push_back({p, offset});
  }
  
  while (!q.empty()) {
    Entry e = q.front();
    Pos p = e.pos;
    int offset = e.offset;
    q.pop_front();

    for (int i = 0; i < 4; i++) {
      Pos nxt = {p.y + dy[i], p.x + dx[i]};
      if (inRange(nxt) && costs[offset][nxt.y][nxt.x] == -1 && map[nxt.y][nxt.x] != WALL) {
        if (map[nxt.y][nxt.x] == DOOR) {
          costs[offset][nxt.y][nxt.x] = costs[offset][p.y][p.x] + 1;
          q.push_back({nxt, offset});
        } else {
          costs[offset][nxt.y][nxt.x] = costs[offset][p.y][p.x];
          q.push_front({nxt, offset});
        }

        rePath[offset][nxt.y][nxt.x] = p;
      }
    }
  }

  int rs = 1000000;
  for (int y = 0; y < h; y++) {
    for (int x = 0; x < w; x++) {
      int sum = 0;
      for (int offset = 0; offset < cnt; offset++) {
        if (costs[offset][y][x] == -1)
          sum = 1000000;

        sum += costs[offset][y][x];
      }

      if (map[y][x] == DOOR) {
        sum -= cnt-1;
      }

      rs = min(rs, sum);
    }
  }

  return rs;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  cin >> T;
  for (int t = 0; t < T; t++) {
    cin >> h >> w;
    h += 2;
    w += 2;
    memset(map[0], EXIT, sizeof(map[0]));
    for (int y = 1; y < h-1; y++) {
      map[y][0] = EXIT;
      cin >> (map[y] + 1);
      map[y][w-1] = EXIT;
    }
    memset(map[h-1], EXIT, sizeof(map[h-1]));

    Pos pos[3];
    pos[0] = {0, 0};
    int offset = 1;
    for (int y = 0; y < h; y++)
      for (int x = 0; x < w; x++)
        if (map[y][x] == MAN)
          pos[offset++] = {y, x};

    int rs = meetEachOthers(pos, 3);

    cout << rs << '\n';
  }

  return 0;
}