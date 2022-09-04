import sys
INF = 10**10
def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))
def print_n(L, join_str=' '):
  for i,l in enumerate(L): print(l, end=join_str if i<len(L)-1 else '\n')
def LL(n,m,d=0): return [[d]*n for _ in range(m)]
def avg(l): return sum(l)/len(l)

def ccw(A, B, C):
	tmp = A[0]*B[1]+B[0]*C[1]+C[0]*A[1] - (A[1]*B[0]+B[1]*C[0]+C[1]*A[0])
	if tmp > 0: return 1
	elif tmp == 0: return 0
	else: return -1
def ck_cross(A, B, C, D):
	ccw_ab = ccw(A, B, C) * ccw(A, B, D)
	ccw_cd = ccw(C, D, A) * ccw(C, D, B)

	if ccw_ab == 0 and ccw_cd == 0:
		return min(A, B) <= min(C, D) <= max(A, B) \
			or min(C, D) <= min(A, B) <= max(C, D)
	else: return ccw_ab <= 0 and ccw_cd <= 0

class UnionFindNode:
	def __init__(self, A, B):
		self.A = A
		self.B = B
		self.parent = self
	def find(self):
		if self.parent != self:
			self.parent = self.parent.find()
		return self.parent
	def union(self, n):
		n.find().parent = self.find()

N = input(int)
A = []
G = []

for _ in range(N):
	x1, y1, x2, y2 = input_n(int)
	X = UnionFindNode((x1,y1), (x2,y2))
	for a in A:
		if ck_cross(X.A, X.B, a.A, a.B): a.union(X)
	A.append(X)

root_dict = {}
for a in A:
	r = a.find()
	if r not in root_dict.keys():
		root_dict[r] = 0
	root_dict[r]+=1
print(len(root_dict.keys()))
print(max(root_dict.values()))