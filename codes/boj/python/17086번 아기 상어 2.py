import sys
sys.setrecursionlimit(100000) # 재귀 제한 풀기

import heapq

# custom heap
class CustomHeap:
	class Node(object):
		def __init__(self, val, comparator=None):
			self.val = val
			self.comparator = comparator

		def __repr__(self):
			return f'Node value: {self.val}'

		def __lt__(self, other):
			if self.comparator:
				return self.comparator(self.val, other.val)
			else:
				return self.val < other.val

	def __init__(self, comparator=None):
		self.heap = []
		self.comparator = comparator

	def push(self, val):
		heapq.heappush(self.heap, CustomHeap.Node(val, self.comparator))

	def pop(self):
		return heapq.heappop(self.heap).val

	def is_empty(self):
		return len(self.heap) == 0
##

def _input():
	return sys.stdin.readline().rstrip()
def _input_n(_type):
	return map(_type, _input().split())

def node_comparator(val1, val2):
	if val1[2] != val2[2]: # dist
		return val1[2] < val2[2]
	elif val1[1] != val2[1]: # y
		return val1[1] < val2[1]
	elif val1[0] != val2[0]: # x
		return val1[0] < val2[0]
	else:
		return True


def find(field, sharks_pos):

	def dequeue(x,y,cur_dist):
		check.dist_field[y][x] = cur_dist
		check.queue.push((x,y,cur_dist))

	def enqueue_neighbor(x,y,cur_dist):
		nebors_pos = [{'x':x-1, 'y':y-1}, {'x':x, 'y':y-1}, {'x':x+1, 'y':y-1},
									{'x':x-1, 'y':y}, {'x':x, 'y':y}, {'x':x+1, 'y':y},
									{'x':x-1, 'y':y+1}, {'x':x, 'y':y+1}, {'x':x+1, 'y':y+1}]

		for nebor_pos in nebors_pos:
			if nebor_pos['y'] < 0 or nebor_pos['y'] >= len(check.dist_field):
				continue

			if nebor_pos['x'] < 0 or nebor_pos['x'] >= len(check.dist_field[0]):
				continue

			if check.dist_field[nebor_pos['y']][nebor_pos['x']] != 0 and check.dist_field[nebor_pos['y']][nebor_pos['x']] <= cur_dist+1: # 이미 탐색함
				continue

			dequeue(x=nebor_pos['x'],y=nebor_pos['y'],cur_dist=cur_dist+1)

	def check(x,y):
		pass

	def next():
		x,y,cur_dist = check.queue.pop()
		enqueue_neighbor(x,y,cur_dist)

	# init dist_field and queue
	check.dist_field = [[0]*len(field[0]) for _ in range(len(field))]
	check.queue = CustomHeap(comparator=node_comparator)
	
	for shark_pos in sharks_pos:
		check.dist_field[shark_pos['y']][shark_pos['x']] = -1 # 상어는 -1로 한다. (탐색 제외)
	for shark_pos in sharks_pos:
		enqueue_neighbor(shark_pos['x'], shark_pos['y'], cur_dist=0)

	while not check.queue.is_empty():
		next()

	max_val = 0
	for line in check.dist_field:
		for val in line:
			max_val = max(max_val, val)

	return max_val


def act():
	N, M = _input_n(int)
	field = []
	sharks_pos = []

	# field mapping
	for y in range(N):
		line = list(_input_n(int))
		for x in range(M):
			if line[x] == 1:
				pos = {'x':0, 'y':0}
				pos['x'] = x
				pos['y'] = y

				sharks_pos.append(pos)
		field.append(line)

	print(find(field, sharks_pos))

act()