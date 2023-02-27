from collections import deque

def solution(board, moves):
    Y, X = len(board), len(board[0])

    tops = [0]*X
    for x in range(X):
        while tops[x] < Y and board[tops[x]][x] == 0:
            tops[x] += 1

    s = deque()
    cnt_pop = 0
    for x in moves:
        x -= 1
        if tops[x] == Y:
            continue

        if s and s[-1] == board[tops[x]][x]:
            s.pop()
            cnt_pop += 2
        else:
            s.append(board[tops[x]][x])
        tops[x] += 1
    return cnt_pop