import sys


def input(_type=str):
    return _type(sys.stdin.readline().strip())


def input_n(_type=str):
    return list(map(_type, input().split()))


N = input(int)
A = input_n(int)
pre_dp = [0] * N
cur_dp = [0] * (N - 1)

for i in range(N - 1):
    if A[i] == A[i + 1]:
        cur_dp[i] = 0
    else:
        cur_dp[i] = 1

for d in range(2, N):
    nxt_dp = [0] * (N - d)
    for left in range(N - d):
        right = left + d

        nxt_dp[left] = min(cur_dp[left] + 1, cur_dp[left + 1] + 1)
        if A[left] == A[right]:
            nxt_dp[left] = min(nxt_dp[left], pre_dp[left + 1])
        else:
            nxt_dp[left] = min(nxt_dp[left], pre_dp[left + 1] + 2)

    pre_dp, cur_dp = cur_dp, nxt_dp

print(cur_dp[0])
