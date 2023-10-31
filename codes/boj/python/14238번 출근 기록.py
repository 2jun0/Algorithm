import sys


def input(_type=str):
    return _type(sys.stdin.readline().strip())


def input_n(_type=str):
    return list(map(_type, input().split()))


S = input()
a_cnt = 0
b_cnt = 0
c_cnt = 0
for s in S:
    if s == "A":
        a_cnt += 1
    elif s == "B":
        b_cnt += 1
    elif s == "C":
        c_cnt += 1

visited = [
    [
        [[[False] * 4 for _ in range(4)] for _ in range(c_cnt + 1)]
        for _ in range(b_cnt + 1)
    ]
    for _ in range(a_cnt + 1)
]
# 50 * 50 * 50 * 3 * 3

A = 1
B = 2
C = 3


def dfs(visited, a_cnt, b_cnt, c_cnt, prev, cur, trace):
    def try_nxt(nxt):
        n_a, n_b, n_c = a_cnt, b_cnt, c_cnt
        n_trace = trace
        if nxt == A:
            n_a -= 1
            n_trace += "A"
        elif nxt == B:
            n_b -= 1
            n_trace += "B"
        elif nxt == C:
            n_c -= 1
            n_trace += "C"

        if not visited[n_a][n_b][n_c][cur][nxt]:
            # 중복 제거
            visited[n_a][n_b][n_c][cur][nxt] = True
            return dfs(visited, n_a, n_b, n_c, cur, nxt, n_trace)

    if a_cnt == 0 and b_cnt == 0 and c_cnt == 0:
        return trace

    rs = None

    if a_cnt > 0:
        rs = rs or try_nxt(A)

    if b_cnt > 0 and cur != B:
        # 오늘 B가 출근했으면 내일은 못해
        rs = rs or try_nxt(B)

    if c_cnt > 0 and cur != C and prev != C:
        # 오늘, 어제 C가 출근했으면 내일은 못해
        rs = rs or try_nxt(C)

    return rs


rs = dfs(visited, a_cnt, b_cnt, c_cnt, 0, 0, "")
if rs:
    print(rs)
else:
    print(-1)
