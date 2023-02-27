from collections import deque
import sys

def input(_type=str):
	return _type(sys.stdin.readline().strip())
def input_n(_type=str):
	return list(map(_type, input().split()))

END = '0'

def make_fail(trie):
  fail = {}
  
  q = deque()
  q.append((fail, trie))
  while q:
    curr, node = q.popleft()
    
    for nxt in node:
      

def add_trie(trie, word):
  curr = trie
  for letter in word:
    curr = curr.setdefault(letter, {})
  curr[END] = END

def get_find_idx(trie, text, srt_idx):
  idx = srt_idx
  find_idx = -1
  
  curr = trie
  for idx in range(srt_idx, len(text)):
    if text[idx] in curr:
      curr = curr[text[idx]]
      
      if END in curr:
        find_idx = idx
    else:
      break
        
  return find_idx

def search(trie, text):
  found = [False]*len(text)
  idx = 0
  
  for idx in range(len(text)):
    find_idx = get_find_idx(trie, text, idx)
    
    if find_idx == -1:
      continue
    
    for fi in range(idx, find_idx+1):
      found[fi] = True
    
  return found.count(True)

N = input(int)
text = input()
M = input(int)

trie = {}
for _ in range(M):
  add_trie(trie, input())

print(len(text) - search(trie, text))