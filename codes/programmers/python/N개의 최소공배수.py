def solution(arr):
  for num in range(1, 1000000000):
    if sum(num % a for a in arr) == 0:
      return num