import sys

def input(type_=str):
	return type_(sys.stdin.readline().rstrip())

def place_queen(y, x, visited, undo=False):
    if undo:
        d = -1
    else:
        d = 1
    
    # 세로
    for ty in range(0, N):
        visited[ty][x] += d
    # 가로
    for tx in range(0, N):
        visited[y][tx] += d
    # 대각 역슬래시
    ty = y - min(y, x)
    tx = x - min(y, x)
    while ty < N and tx < N:
        visited[ty][tx] += d
        ty += 1
        tx += 1
    
    # 대각 슬래시
    ty = y - min(y, N-1-x)
    tx = x + min(y, N-1-x)
    while ty < N and 0 <= tx:
        visited[ty][tx] += d
        ty += 1
        tx -= 1
    
    # remove duplicated
    visited[y][x] -= 3*d

def dfs(y, x, visited, cnt):
    if cnt == N:
        return 1
    
    place_queen(y, x, visited)
    
    cnts = 0
    
    for nx in range(N):
        if visited[y+1][nx] == 0:
            # can place?
            cnts += dfs(y+1, nx, visited, cnt+1)
    
    place_queen(y, x, visited, undo=True)
    return cnts

N = input(int)
visited = [[0]*N for _ in range(N)]
total_cnt = 0
for x in range(N):
    total_cnt += dfs(0, x, visited, 1)
        
print(total_cnt)