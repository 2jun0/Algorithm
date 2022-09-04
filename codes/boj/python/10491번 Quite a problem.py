import sys

for L in sys.stdin:
  L = L.strip().lower()
  if 'problem' in L: print('yes')
  else: print('no')