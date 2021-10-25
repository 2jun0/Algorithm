import sys
sys.setrecursionlimit(10000000) # 재귀 제한 풀기

def _input(_type=str):
	return _type(sys.stdin.readline().rstrip())
def _input_n(_type):
	return map(_type, _input().split())

class Shark:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
		self.is_eaten = False
		self.eaten_by = None
		self.targets = []

	def __lt__(self, other):
		if self.a != other.a:
			return self.a > other.a
		elif self.b != other.b:
			return self.b > other.b
		elif self.c != other.c:
			return self.c > other.c
		else:
			return True

	def __repr__(self):
		if self.is_eaten:
			return f'a:{self.a},b:{self.b},c:{self.c},eaten by:{self.eaten_by}'
		else:
			return f'a:{self.a},b:{self.b},c:{self.c}'

sharks = []
def dfs(idx):
	global sharks

	for target in sharks[idx].targets:
		if dfs.check[target]:
			continue

		dfs.check[target] = True
		
		if not sharks[target].is_eaten or dfs(sharks[target].eaten_by): # 누가 이미 먹었으면 뺏어먹을 수 있는지 확인
			sharks[target].is_eaten = True
			sharks[target].eaten_by = idx
			return True

	return False
dfs.check = []

def find_target(idx):
	global sharks
	
	for i, shark in enumerate(sharks):
		if i == idx:
			continue

		if sharks[idx].a == sharks[i].a and sharks[idx].b == sharks[i].b and sharks[idx].c == sharks[i].c and idx < i:
			continue

		if sharks[idx].a >= sharks[i].a and sharks[idx].b >= sharks[i].b and sharks[idx].c >= sharks[i].c:
			sharks[idx].targets.append(i)

def act():
	global sharks
	N = _input(int)

	for _ in range(N):
		a,b,c = _input_n(int)
		sharks.append(Shark(a,b,c))

	for i in range(N):
		find_target(i)

	for _ in range(2):
		for i in range(N):
			dfs.check = [False]*N
			dfs(i)

	eaten_shark_cnt = 0
	for shark in sharks:
		if shark.is_eaten: eaten_shark_cnt += 1

	print(len(sharks) - eaten_shark_cnt)

act()