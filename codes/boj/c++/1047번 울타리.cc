#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

struct Tree {
  int y;
  int x;
  int size;
};

int N;
vector<Tree> trees;

int minCuttedTreeCnt(int ySrt, int yEnd, int xSrt, int xEnd) {
  struct compare {
    bool operator()(Tree a, Tree b) {
      return a.size < b.size;
    }
  };
  priority_queue<Tree, vector<Tree>, compare> selected;
  int wanted = 2*(yEnd-ySrt) + 2*(xEnd-xSrt);
  int cutCnt = 0;

  for (Tree& t: trees) {
    if (ySrt <= t.y && t.y <= yEnd && xSrt <= t.x && t.x <= xEnd) {
      selected.push(t);
    } else {
      wanted -= t.size;
      cutCnt ++;
    }
  }

  while (wanted > 0 && !selected.empty()) {
    Tree t = selected.top();
    selected.pop();

    wanted -= t.size;
    cutCnt ++;
  }

  if (wanted > 0) {
    return 100;
  } else {
    return cutCnt;
  }
}

bool treeCmpYAsc (Tree a, Tree b) { return a.y < b.y; }
bool treeCmpXAsc (Tree a, Tree b) { return a.x < b.x; }

int main() {
  cin >> N;

  for (int i = 0; i < N; i++) {
    Tree t;
    cin >> t.y >> t.x >> t.size;
    trees.push_back(t);
  }

  vector<Tree> yTrees = trees;
  sort(yTrees.begin(), yTrees.end(), treeCmpYAsc);

  vector<Tree> xTrees = trees;
  sort(xTrees.begin(), xTrees.end(), treeCmpXAsc);

  int rs = 100;
  for (int ySrtIdx = 0; ySrtIdx < N; ySrtIdx++) {
    int ySrt = yTrees[ySrtIdx].y;
    for (int yEndIdx = ySrtIdx; yEndIdx < N; yEndIdx++) {
      int yEnd = yTrees[yEndIdx].y;
      for (int xSrtIdx = 0; xSrtIdx < N; xSrtIdx++) {
        int xSrt = xTrees[xSrtIdx].x;
        for (int xEndIdx = xSrtIdx; xEndIdx < N; xEndIdx++) {
          int xEnd = xTrees[xEndIdx].x;

          rs = min(rs, minCuttedTreeCnt(ySrt, yEnd, xSrt, xEnd));
        }
      }
    }
  }

  cout << rs << '\n';

  return 0;
}