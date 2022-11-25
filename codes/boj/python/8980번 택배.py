import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

def get_accept_weight(remain_list, from_num, to_num, weight):
  '''from_num ~ to_num에서 weight를 실고 싶을 때, 가능한 무게'''
  accept_weight = weight

  for num in range(from_num, to_num):
    accept_weight = min(accept_weight, remain_list[num])
  
  return accept_weight

N, C = input_n(int)
M = input(int)
infos = []

for _ in range(M):
  from_num, to_num, weight = input_n(int)
  infos.append((from_num, to_num, weight))

# 택배는 도착지가 가까운 것 먼저!
infos.sort(key=lambda x: (x[1], x[0]))

remain_list = [C]*(N+1)
sum_carry = 0

for from_num, to_num, weight in infos:
  accept_weight = get_accept_weight(remain_list, from_num, to_num, weight)
  sum_carry += accept_weight

  for num in range(from_num, to_num):
    remain_list[num] -= accept_weight

print(sum_carry)