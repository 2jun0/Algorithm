from itertools import combinations
import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_kill_cnt(archer_poses):
  '''archer_poses에 따른 게임 플레이 결과 구하기'''
  # 여기서! 효율적인 방법이 뭘까??
  kill_cnt = 0
  enemy_poses = [(y,x) for x in range(M) for y in range(N) if table[y][x] == 1]

  while len(enemy_poses) > 0:
    # 모든 적이 사라질 때까지 반복

    # 궁수들이 화살을 맞추는 위치를 구함 -> 적의 위치를 구하는 것.
    target_poses = set()

    for archer_x in archer_poses:
      # 가장 가까운 적을 구함
      # 우선순위는, 거리 -> 왼쪽 순
      enemy_pos = sorted(
        enemy_poses,
        key=lambda pos: (N - pos[0] + abs(archer_x - pos[1]), pos[1])
      )[0]

      # 쏠 수 있는 거리여야함.
      if N - enemy_pos[0] + abs(archer_x - enemy_pos[1]) <= D:
        target_poses.add(enemy_pos)

    # 적을 쏘아 맞추기
    kill_cnt += len(target_poses)
    for target_pos in target_poses:
      enemy_poses.remove(target_pos)

    # 적이 아래로 움직임
    nxt_enemy_poses = []
    for enemy_y, enemy_x in enemy_poses:
      if enemy_y < N-1:
        # 마지막이 아닌경우만 움직임
        nxt_enemy_poses.append((enemy_y+1,enemy_x))
    enemy_poses = nxt_enemy_poses
  
  return kill_cnt

N, M, D = input_n(int)
table = [input_n(int) for _ in range(N)]

max_kill_cnt = 0
for archer_poses in combinations(range(M), 3):
  max_kill_cnt = max(max_kill_cnt, get_kill_cnt(archer_poses))

print(max_kill_cnt)
