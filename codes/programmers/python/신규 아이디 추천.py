def solution(id):
  alphas = [chr(i) for i in range(ord('a'), ord('z')+1)] 
  numbers = [str(i) for i in range(0,10)]

  # step 1
  id = id.lower()
  
  new_id = ''
  for c in id:
    # step 2
    if c not in alphas and c not in ['-','_','.'] and c not in numbers:
      continue
    
    # step 3
    if len(new_id) > 0 and new_id[-1] == '.' and c == '.':
      continue

    new_id += c
  id = new_id

  # step 4
  while len(id) > 0 and id[0] == '.':
    if len(id) > 1:
      id = id[1:]
    else:
      id = ''
  while len(id) > 0 and id[-1] == '.':
    if len(id) > 1:
      id = id[:-1]
    else:
      id = ''

  # step 5
  if not id:
    id = 'a'

  # step 6
  if len(id) >= 16:
    id = id[:15]
  while len(id) > 0 and id[-1] == '.':
    if len(id) > 1:
      id = id[:-1]
    else:
      id = ''
  
  # step 7
  while len(id) <= 2:
    id += id[-1]
  
  return id