INF = 10**10
idx2score = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def get_scores(apeach_info, lion_info):
  '''어피치 점수와 라이언 점수 구하기'''
  apeach_score, lion_score = 0, 0
  for idx in range(11):
    if lion_info[idx] + apeach_info[idx]  == 0:
      # 둘다 0인 경우 제외
      continue

    if lion_info[idx] > apeach_info[idx]:
      lion_score += idx2score[idx]
    else:
      apeach_score += idx2score[idx]
  
  return apeach_score, lion_score

def get_optimal_info(a_info, b_info):
  '''a_info와 b_info 중에 어떤 것이 더 답에 적합한지 구함'''

  for idx in range(10, -1, -1):
    if a_info[idx] > b_info[idx]:
      return a_info
    elif a_info[idx] < b_info[idx]:
      return b_info
  
  return a_info

def solution(n, apeach_info):
  max_diff = -INF
  optimal_lion_info = None

  def dfs(idx, total_cnt, lion_info):
    '''lion_info 구하는 dfs 함수..'''
    nonlocal max_diff, optimal_lion_info

    if idx == 11:
      if total_cnt != n:
        lion_info[10] += n - total_cnt

      apeach_score, lion_score = get_scores(apeach_info, lion_info)
      diff = lion_score - apeach_score

      if max_diff < diff:
        max_diff = diff
        optimal_lion_info = lion_info
      elif max_diff == diff:
        optimal_lion_info = get_optimal_info(optimal_lion_info, lion_info)

      return

    # idx에 얼마나 많은 화살을 맞춰야 하나?
    require_cnt = apeach_info[idx]+1

    # Branch 1 : idx에 맞춤
    if total_cnt+require_cnt <= n:
      nxt_lion_info = lion_info[::]
      nxt_lion_info[idx] = require_cnt
      dfs(idx+1, total_cnt+require_cnt, nxt_lion_info)

    # Branch 2 : idx에 안 맞춤
    dfs(idx+1, total_cnt, lion_info)

  dfs(0, 0, [0]*11)

  return optimal_lion_info if max_diff > 0 else [-1]