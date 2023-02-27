#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

struct Expr {
  string label;
  vector<pair<int, string> > attrs;
  int waitAttrCnt = 0;
};

int N, M;
map<string, long long> prices;
vector<Expr*> exprs;

map<string, vector<Expr*> > attrToExprs;
map<string, vector<Expr*> > labelToExprs;
map<string, int> waittingCnt;

const long long INIT = 1000000002l;
const long long MAX = 1000000001l;

Expr* parse(string s) {
  int i = 0;

  Expr* expr = new Expr();
  for (; i < s.size() && s[i] != '='; i++) {
    expr -> label += s[i];
  }
  i++;

  while (i < s.size()) {
    pair<int, string> attr;
    // 지수 쓰기
    attr.first = s[i++]-'0';
    for (; i < s.size() && s[i] != '+'; i++) {
      attr.second += s[i];
    }
    i++; // ignore +

    expr -> attrs.push_back(attr);
    attrToExprs[attr.second].push_back(expr);
  }

  expr -> waitAttrCnt = expr -> attrs.size();
  waittingCnt[expr -> label]++;
  labelToExprs[expr -> label].push_back(expr);

  return expr;
}


void solveExpr(Expr* expr);
/**
 * 식이 해결되었을때 호출
*/
void resolveExpr(Expr* expr) {
  if (--waittingCnt[expr->label] == 0) {
    for (Expr* nxtExpr : attrToExprs[expr->label]) {
      nxtExpr->waitAttrCnt--;

      if (nxtExpr->waitAttrCnt == 0) {
        solveExpr(nxtExpr);
      }
    }
  }
}

/**
 * 식을 풀음
*/
void solveExpr(Expr* expr) {
  long long price = 0;

  for (pair<int, string> p: expr->attrs) {
    price = min(price + p.first * prices[p.second], MAX);
  }

  prices[expr->label] = min(prices[expr->label], price);
  resolveExpr(expr);
}

/**
 * prices 초기화
*/
void initPrices() {
  for (const Expr* expr : exprs) {
    if (!prices[expr -> label]) {
      prices[expr -> label] = INIT;
    }

    for (const pair<int, string>& p : expr -> attrs) {
      if (!prices[p.second]) {
        prices[p.second] = INIT;
      }
    }
  }
}

bool getMinPriceWaittingLabel(string& label) {
  int minPrice = INIT;
  for(const pair<string, long long> &p : prices) {
    if (waittingCnt[p.first] > 0 && p.second < minPrice) {
      label = p.first;
      minPrice = p.second; 
    }
  }
  return minPrice != INIT;
}

int main() {
  cin >> N >> M;
  prices["one"] = 1;

  for (int i = 0; i < N; i++) {
    string label;
    int p;
    cin >> label >> p;

    Expr *e = new Expr();
    e->label = label;
    pair<int, string> attr(p, "one");
    e->attrs.push_back(attr);
    waittingCnt[label] = 1;
    exprs.push_back(e);
  }

  for (int i = 0; i < M; i++) {
    string s;
    cin >> s;

    Expr* e = parse(s);
    exprs.push_back(e);
  }

  initPrices();

  for (Expr* e : exprs) {
    if (e -> waitAttrCnt == 0) {
      solveExpr(e);
    }
  }

  string label;
  while (getMinPriceWaittingLabel(label)) {
    for (Expr *e : labelToExprs[label]) {
      if (e->waitAttrCnt > 0) {
        e->waitAttrCnt = 0;
        solveExpr(e);
      }
    }
  }

  if (prices["LOVE"] == INIT || prices["LOVE"] == 0)
    cout << -1 << '\n';
  else
    cout << prices["LOVE"] << '\n';

  return 0;
}