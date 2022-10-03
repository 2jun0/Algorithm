from collections import deque
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_closest_client_pos_and_cost(taxi_y, taxi_x, fuel):
  '''가장 가짜운 고객의 좌표와 비용 찾기
  - 찾은 경우 : 고객의 좌표(tuple), 비용
  - 못 찾은 경우 : (-1,-1), -1
  '''
  costs = [[-1]*N for _ in range(N)]
  q = deque()

  costs[taxi_y][taxi_x] = 0
  q.append((taxi_y, taxi_x))

  # 후보군
  candidates = []

  while q:
    y, x = q.popleft()

    if client_table[y][x] != 0:
      candidates.append((costs[y][x],y,x))

    if len(candidates) > 0:
      # 후보군이 선출되면 다음 레벨로 이동할 수 없다.
      continue

    for n_y, n_x in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
      if 0<=n_y<N and 0<=n_x<N and costs[n_y][n_x] == -1 and not is_wall[n_y][n_x] and costs[y][x]+1 <= fuel:
        costs[n_y][n_x] = costs[y][x] + 1
        q.append((n_y,n_x))
  
  if len(candidates) > 0:
    # 후보군 중, 한명의 고객 선출
    candidates.sort()
    _, client_y, client_x = candidates[0]
    return (client_y, client_x), costs[client_y][client_x]
  else:
    return (-1,-1),-1

def get_dest_pos_and_cost(taxi_y, taxi_x, fuel, client_num):
  '''고객의 목적지 좌표, 목적지까지 비용 찾기
  - 갈 수 있는 경우 : 목적지 좌표(tuple), 비용
  - 못 가는 경우 : (-1,-1), -1
  '''
  costs = [[-1]*N for _ in range(N)]
  q = deque()

  costs[taxi_y][taxi_x] = 0
  q.append((taxi_y, taxi_x))

  while q:
    y, x = q.popleft()

    if client_num in dest_table[y][x]:
      return (y,x), costs[y][x]

    for n_y, n_x in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
      if 0<=n_y<N and 0<=n_x<N and costs[n_y][n_x] == -1 and not is_wall[n_y][n_x] and costs[y][x]+1 <= fuel:
        costs[n_y][n_x] = costs[y][x] + 1
        q.append((n_y,n_x))

  return (-1,-1),-1

N, M, fuel = input_n(int)
# 벽이 있는지 여부
is_wall = [[
    True if a == 1 else False
    for a in input_n(int)
  ] for _ in range(N)]
# 고객 테이블 (고객 번호 or 0(없다))
client_table = [[0]*N for _ in range(N)]
# 목적지 테이블 (배열) 
dest_table = [[[] for _ in range(N)] for _ in range(N)]

taxi_pos = [a-1 for a in input_n(int)]

# init client, dest table
for client_num in range(1,M+1):
  _client_y, _client_x, _dest_y, _dest_x = input_n(int)
  client_y, client_x, dest_y, dest_x = _client_y-1, _client_x-1, _dest_y-1, _dest_x-1

  client_table[client_y][client_x] = client_num
  dest_table[dest_y][dest_x].append(client_num)

go_client_cnt = 0
go_dest_cnt = 0
while True:
  '''가까운 고객 찾기'''
  client_pos, cost = get_closest_client_pos_and_cost(*taxi_pos, fuel)
  if cost == -1:
    # 못 찾았다.
    break

  go_client_cnt += 1

  client_y, client_x = client_pos
  client_num = client_table[client_y][client_x]

  client_table[client_y][client_x] = 0
  taxi_pos = client_pos

  fuel -= cost

  '''고객 목적지 찾기'''
  dest_pos, cost = get_dest_pos_and_cost(*taxi_pos, fuel, client_num)
  if cost == -1:
    # 못 간다.
    break
  
  go_dest_cnt += 1
  taxi_pos = dest_pos

  fuel += cost

print(fuel if go_client_cnt == M and go_dest_cnt == M else -1)