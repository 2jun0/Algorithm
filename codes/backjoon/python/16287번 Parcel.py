import sys
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

# 그냥 구하면 5000C4 => 너무 큼
# 쪼개면 줄어든다. 5000C2 * 2 => 3천만 정도

# 쪼개는 방법
# 4:0 => recurvice
# 3:1 => recurvice
# 2:2
# 1:3 => recurvice
# 4:0 => recurvice


w, n = input_n(int)
A = input_n(int)
A.sort(reverse=True)

#########################

# 틀린 문제!!

#########################