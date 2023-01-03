import sys

def input(_type=str):
  return _type(sys.stdin.readline().strip())
def input_n(_type=str):
  return list(map(_type, input().split()))

N, M = input_n(int)
P = input_n(int)
if (N == 1 and M == 2) or (N == 2 and M == 1):
  print('ChongChong')
else:
  print('GomGom')

'''
# 1X2 인 경우, 1X1을 똑같이 놔야 한다. 고로 총총이의 승리

# 이외의 경우, 가운데를 놓아서 유리하게 만든다.
## N과 M이 모두 홀수
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0   가운데에 놓으면 매우 유리하게 시작한다.
0 0 0 0 0   곰곰이는 총총이의 수를 배껴서 x축 대칭으로 두면 승리
0 0 0 0 0

## N과 M이 모두 짝수
0 0 0 0
0 1 1 0  가운데에 놓으면 매우 유리하게 시작한다.
0 1 1 0  곰곰이는 총총이의 수를 배껴서 x축 대칭으로 두면 승리 
0 0 0 0  

## 둘중 하나만 짝수인 경우
0 0 1 0
0 1 1 0  계단 모양의 블럭을 가운데로 두어서 반으로 나누자. 
0 1 0 0

1 1 1 1  홀수가 1인 경우 한방에 이기는 것은 자명하다.
'''