import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기

def _input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def _input_n(_type):
	return list(map(_type, _input().split()))

def main():
	T = _input(int)
	for _ in range(T):
		Nd2, W = _input_n(int)

		e1 = _input_n(int)
		e2 = _input_n(int)

		a = [0]*100000
		b = [0]*100000
		c = [0]*100000

		def solve(t):
			for i in range(t, Nd2):
				a[i+1] = 1000000

				# case 1
				if e1[i] + e2[i] <= W:
					a[i+1] = a[i] + 1
				# case 2
				if i > 0 and e1[i-1] + e1[i] <= W and e2[i-1] + e2[i] <= W:
					a[i+1] = min(a[i+1], a[i-1] + 2)
				# case 3
				a[i+1] = min(a[i+1], b[i] + 1)
				# case 4
				a[i+1] = min(a[i+1], c[i] + 1)

				if i < Nd2-1:
					b[i+1] = c[i+1] = 10000000

					b[i+1] = a[i+1] + 1
					if e1[i] + e1[i+1] <= W:
						b[i+1] = min(b[i+1], c[i] + 1)
					c[i+1] = a[i+1] + 1
					if e2[i] + e2[i+1] <= W:
						c[i+1] = min(c[i+1], b[i] + 1)

		a[0] = 0
		b[0] = 1
		c[0] = 1

		solve(0)
		res = a[Nd2]

		if Nd2 > 1 and e1[0] + e1[-1] <= W:
			a[1] = 1
			b[1] = 2
			c[1] = 1 if e2[0] + e2[1] <= W else 2
			solve(1)
			res = min(res, c[Nd2-1] + 1)

		if Nd2 > 1 and e2[0] + e2[-1] <= W:
			a[1] = 1
			b[1] = 1 if e1[0] + e1[1] <= W else 2
			c[1] = 2
			solve(1)
			res = min(res, b[Nd2-1] + 1)

		if Nd2 > 1 and e1[0] + e1[-1] <= W and e2[0] + e2[-1] <= W:
			a[1] = 0
			b[1] = 1
			c[1] = 1
			solve(1)
			res = min(res, a[Nd2-1] + 2)

		print(res)

main()