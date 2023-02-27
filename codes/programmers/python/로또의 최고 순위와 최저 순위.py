def solution(lottos, win_nums):
    have = [False] * 50
    for num in win_nums:
      have[num] = True
    
    match_cnt = 0
    for num in lottos:
      if have[num]:
        match_cnt += 1

    return [min(6-(match_cnt+lottos.count(0))+1, 6), min(6-match_cnt+1, 6)]