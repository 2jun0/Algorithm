import sys

def input(type=str):
  return type(sys.stdin.readline().strip())
def input_n(type=str):
  return list(map(type, input().split()))

def can_watch(srt):
  # 긴것 부터 묶는다.
  # 짧은 그룹부터 본다.
  # 무 조 건 K로 묶는게 이득이다. 그냥 이득임 이대로 해!
  groups = []
  for srt_i in range(srt, N, K):
    groups.append(L[srt_i])
    
  total = 0
  for i in range(len(groups) - 1, -1, -1):
    total += groups[i]
    
  return total <= M

def find_cnt():
  srt, end = 0, len(L)-1
  
  # 커질 수록 True가 될 확률이 올라간다.
  while srt < end:
    mid = (srt + end) // 2
    
    if can_watch(mid):
      end = mid
    else:
      srt = mid + 1
  if can_watch(end):
    return len(L) - end
  else:
    return 0

N, M, K = input_n(int)
L = input_n(int)
L.sort(reverse=True)
print(find_cnt())
  