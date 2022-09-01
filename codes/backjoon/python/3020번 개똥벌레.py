import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

N, H = input_n(int)
even_obs_cnt = [0]*(H+1)
odd_obs_cnt = [0]*(H+1)
obs_cnt = [0]*(H+1)

for x in range(N):
  if x % 2 == 0:
    even_obs_cnt[input(int)] += 1
  else:
    odd_obs_cnt[H-input(int)+1] += 1

for height in range(H, 1, -1):
  even_obs_cnt[height-1] += even_obs_cnt[height]
for height in range(1, H):
  odd_obs_cnt[height+1] += odd_obs_cnt[height]

for height in range(1, H+1):
  obs_cnt[height] = even_obs_cnt[height] + odd_obs_cnt[height]

obs_cnt[0] = 10**10
  
min_cnt = min(obs_cnt)
case_cnt = obs_cnt.count(min_cnt)

print(min_cnt, case_cnt)