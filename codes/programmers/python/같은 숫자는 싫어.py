def solution(arr):
  new_arr = [arr[0]]
  for val in arr:
    if new_arr[-1] != val:
      new_arr.append(val)
  
  return new_arr