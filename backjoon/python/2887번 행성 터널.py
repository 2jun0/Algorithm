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

N = input(int)

class UnionFindNode:
	def __init__(self, x, y, z):
		self.x, self.y, self.z = x,y,z
		self.parent = self
	def find(self):
		if self.parent != self:
			self.parent = self.parent.find()
		return self.parent
	def union(self, n):
		n.find().parent = self.find()
	def __lt__(self, n):
		return self.x < n.x


Ax = []
Ay = []
Az = []

for i in range(N):
	x,y,z = input_n(int)
	a = UnionFindNode(x,y,z)
	Ax.append((x, a))
	Ay.append((y, a))
	Az.append((z, a))

Ax.sort()
Ay.sort()
Az.sort()

E = []

for i in range(N-1):
	_, a1 = Ax[i]
	_, a2 = Ax[i+1]
	d = abs(a1.x-a2.x)
	E.append((d, a1, a2))

for i in range(N-1):
	_, a1 = Ay[i]
	_, a2 = Ay[i+1]
	d = abs(a1.y-a2.y)
	E.append((d, a1, a2))

for i in range(N-1):
	_, a1 = Az[i]
	_, a2 = Az[i+1]
	d = abs(a1.z-a2.z)
	E.append((d, a1, a2))

E.sort()

sum_d = 0
for d, a1, a2 in E:
	if a1.find() != a2.find():
		a1.union(a2)
		sum_d += d

print(sum_d)