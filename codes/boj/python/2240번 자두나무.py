from shutil import move
import sys
def input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def input_n(_type):
	return list(map(_type, input().split()))

T, W = input_n(int)
cnts = [[[-1]*2 for _ in range(W+1)] for _ in range(T+1)]
cnts[0][0][0] = 0

for turn in range(1,T+1):
  _c_tree_idx = input(int)
  curr_tree_idx = _c_tree_idx - 1
  other_tree_idx = 0 if curr_tree_idx == 1 else 1

  # curr_tree로 이동함
  for move_cnt in range(W+1):
    # 이동하지 않은 케이스 curr_tree_idx -> curr_tree_idx
    if cnts[turn-1][move_cnt][curr_tree_idx] != -1:
      cnts[turn][move_cnt][curr_tree_idx] = max(cnts[turn][move_cnt][curr_tree_idx], cnts[turn-1][move_cnt][curr_tree_idx] + 1)
    # 이동한 케이스 other_tree_idx -> curr_tree_idx
    if move_cnt+1 < W+1 and cnts[turn-1][move_cnt][other_tree_idx] != -1:
      cnts[turn][move_cnt+1][curr_tree_idx] = max(cnts[turn][move_cnt+1][curr_tree_idx], cnts[turn-1][move_cnt][other_tree_idx] + 1)
  
  # curr_tree로 이동하지 않음
  for move_cnt in range(W+1):
    # 이동하지 않은 케이스 other_tree_idx -> other_tree_idx
    if cnts[turn-1][move_cnt][other_tree_idx] != -1:
      cnts[turn][move_cnt][other_tree_idx] = max(cnts[turn][move_cnt][other_tree_idx] , cnts[turn-1][move_cnt][other_tree_idx])
    # 이동한 케이스 curr_tree_idx -> other_tree_idx
    if move_cnt+1 < W+1 and cnts[turn-1][move_cnt][curr_tree_idx] != -1:
      cnts[turn][move_cnt+1][other_tree_idx] = max(cnts[turn][move_cnt+1][other_tree_idx], cnts[turn-1][move_cnt][curr_tree_idx])

print(max(0, max(max(max(a for a in b) for b in c) for c in cnts)))