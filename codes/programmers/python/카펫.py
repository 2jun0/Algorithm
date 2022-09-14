def solution(brown, yellow):
  answer = []

  size = brown + yellow
  for width in range(3,int(size**0.5+1)):
    if size % width == 0:
      height = size // width

      if (width-2) * (height-2) == yellow:
        answer = [max(width, height), min(width, height)]
        break
  
  return answer