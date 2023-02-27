# choice 별 mbti 추가값
DELTA_MBTI_BY_CHOICES = [
  None,
  (3,0),
  (2,0),
  (1,0),
  (0,0),
  (0,1),
  (0,2),
  (0,3),
]
# MBTI ?
def solution(survey, choices):
  mbti = {
    'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J':0, 'M':0, 'A':0, 'N':0
  }

  for cmd, choice in zip(survey, choices):
    d1, d2 = DELTA_MBTI_BY_CHOICES[choice]

    mbti[cmd[0]] += d1
    mbti[cmd[1]] += d2

  result = ''
  # A가 라이언형(R)이라면 B는 튜브형(T)
  for A, B in [('R','T'),('C','F'),('J','M'),('A','N')]:
    if mbti[A] >= mbti[B]:
      result += A
    else:
      result += B
  return result