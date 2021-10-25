import heapq

def factorial(x, div):
	result = 1
	for i in range(2, x+1):
		result = (result * (i % div)) % div
	return result

# def gcd(a, b): # 최대공약수 구하기
# 	# 유클리드 호제법을 사용함.
# 	num = max(a,b)
# 	div = min(a,b)

# 	while (num % div) != 0:
# 		remain = num % div
# 		num = div
# 		div = remain
# 	return div

class UnionFindNode:
  def __init__(self):
    self.parent = self

  def union(self, node):
    node.parent.find().parent = self.find()
  
  def find(self):
    if self.parent != self:
      self.parent = self.parent.find() # 최적화
    return self.parent

##

def exp_mod(num, exp, div):
	x = 1
	pow = num % div

	while exp > 0:
		if exp % 2 == 1:
			x = (x*pow) % div
		pow = (pow*pow) % div	
		exp >>= 1

	return x

# def get_primitive_root(q):
#   """get primitive root number"""

#   for _ in range(100000):
#     num = get_random_coprime(q, q)
#     if pow(num, q-1, q) == 1:
#       return num
  

# def order(a, q):
#   """Calculate a order of a in modulo q"""
#   factors = factorize(q-1)
#   for factor in factors:
#     if pow(a, factor, q) == 1:
#       return factor


# def factorize(n: int) -> typing.List[int]:
#   factor_list = []
#   if not n & 1:
#     factor_list.append(2)
#     while not n & 1:
#       n >>= 1
  
#   composites = [n]

#   while len(composites) > 0:
#     # Get one of factors
#     num = composites.pop(0)

#     # Factor is 1
#     if num == 1:
#       continue

#     # Factor is a prime number 
#     if is_prime(num):
#       factor_list.append(num)
#       continue

#     factor = pollard_rho(num, f=_rho_f1)

#     # Failure 
#     if factor == False:
#       # so, find other way
#       factor = pollard_rho(num, f=_rho_f2)

#     # Failure 
#     if factor == False:
#       # so, find other way
#       factor = pollard_rho(num, f=_rho_f3)
    
#     if factor == False:
#       print(factor, num)
#       raise RuntimeError(f'unable to find factor of {num}')
    
#     composites.append(factor)
#     composites.append(int(num//factor))
    
#   return factor_list

# def _rho_f1(x: int, n: int) -> int:
#   return (x*x - 1) % n
# def _rho_f2(x: int, n: int) -> int:
#   return (x*x + 1) % n
# def _rho_f3(x: int, n: int) -> int:
#   return (x*x + 2) % n

# def pollard_rho(n: int, f =_rho_f2) -> int:
#   """Pollard Rho algorithm method

#   :n = Target number
#   :f = f1 or f2

#   """
  
#   d = 1
#   x1 = x2 = 2

#   while d == 1:
#     x1 = f(x1, n)
#     x2 = f(f(x2, n), n)
#     d = gcd(abs(x1-x2), n)

#   if d == n:
#     return False # Failure
#   else: 
#     return d

# custom heap
class CustomHeap:
	class Node(object):
		def __init__(self, val, comparator=None):
			self.val = val
			self.comparator = comparator
			self.is_deleted = False

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
		
	def __len__(self):
		return len(self.heap)
##

# custom iterator
class CustomIterator:
	class Controller:
		def __init__(self, iter):
			self._iter = iter
		def back(self):
			if self._iter.cur >= 0: self._iter.cur -= 1
		def next(self):
			if self._iter.cur < len(self._iter.array): self._iter.cur += 1
		def del_idx(self, idx): # 실제로 삭제되는 건 아님 그냥 삭제후 인덱스 처리
			if self._iter.end > idx: 
				self._iter.end -= 1
			if self._iter.start >= idx: 
				self._iter.start -= 1
			if self._iter.cur >= idx: 
				self._iter.cur -= 1
		def add_idx(self, idx): # 실제로 추가 건 아님 그냥 추가후 인덱스 처리
			if self._iter.end > idx: 
				self._iter.end += 1
			if self._iter.start >= idx: 
				self._iter.start += 1
			if self._iter.cur >= idx: 
				self._iter.cur += 1
		def get_cur(self): return self._iter.cur
	def __init__(self, array, param1=None, param2=None):
		if param2:
			self.end = param2
			self.start = param1
		else: 
			self.start = 0
			self.end = param1 if param1 else len(array)

		self.array = array
		self.cur = self.start-1
		self.controller = CustomIterator.Controller(self)
	def __iter__(self):
		return self
	def __next__(self):
		self.cur += 1
		if self.cur < self.end:
			return self.array[self.cur], self.controller
		else:
			raise StopIteration
##

class Pointer:
  def __init__(self, x, idx):
    self.x = x
    self.idx = idx
  def __lt__(self, other):
    return (self.x, other.idx) < (other.x, other.idx)
  @classmethod
  def to_pointer_list(cls, L):
    return [Pointer(l, i) for i, l in enumerate(L)]

def LN(ns,d=0,l=0): 
  if l == len(ns): return d
  else: return [LN(ns,d,l+1) for _ in range(ns[l])]
class FactorialArray:
	def __init__(self, n, d):
		self.arr = LN([i for i in range(n,0,-1)], d)
	def get(self, idxes):
		pass_idx_cnt = [0]*len(self.arr)
		V = self.arr
		for idx in idxes:
			V = V[idx-pass_idx_cnt[idx]]
			for i in range(idx, len(pass_idx_cnt)):
				pass_idx_cnt[i] += 1
		return V
	def set(self, idxes, value):
		pass_idx_cnt = [0]*len(self.arr)
		V = self.arr
		for idx in idxes[:-1]:
			V = V[idx-pass_idx_cnt[idx]]
			for i in range(idx, len(pass_idx_cnt)):
				pass_idx_cnt[i] += 1
		V[idxes[-1]] = value