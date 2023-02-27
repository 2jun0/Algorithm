from collections import deque

def solution(q1, q2):
  sum1 = sum(q1)
  sum2 = sum(q2)

  q1 = deque(q1)
  q2 = deque(q2)

  turn = 0
  while turn < (len(q1) + len(q2)) * 2:
    if sum1 > sum2 and q1:
      v = q1.popleft()
      q2.append(v)
      sum1 -= v
      sum2 += v
    elif sum1 < sum2 and q2:
      v = q2.popleft()
      q1.append(v)
      sum2 -= v
      sum1 += v
    elif sum1 == sum2:
      break
    
    turn += 1
  else:
    turn = -1

  return turn