import sys
from collections import defaultdict


def input(type_=str):
    return type_(sys.stdin.readline().rstrip())


def input_n(type_):
    return list(map(type_, input().split()))


def concat_files(files, idx):
    sum_v = files[idx] + files[idx + 1]
    return (*files[:idx], sum_v, *files[idx + 2 :]), sum_v


MAX = 10**10
T = input(int)

for _ in range(T):
    K = input(int)
    A = tuple(input_n(int))
    # K = 500
    # A = tuple(range(500))

    dp = [[MAX] * K for _ in range(K)]
    sum = [[0] * K for _ in range(K)]

    for i in range(K):
        dp[i][i] = 0
        sum[i][i] = A[i]

    for diff in range(1, K):
        for left in range(0, K - diff):
            right = left + diff

            for mid in range(left, right):
                sum[left][right] = sum[left][mid] + sum[mid + 1][right]

                # left ~ mid, mid+1 ~ right
                challenger = dp[left][mid] + dp[mid + 1][right] + sum[left][right]
                dp[left][right] = min(dp[left][right], challenger)

    print(dp[0][K - 1])
