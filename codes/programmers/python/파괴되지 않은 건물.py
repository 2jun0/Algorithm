DEMENSION_X = 1
DEMENSION_Y = 0

class Node:
  def __init__(self, srt, end, v, demension):
    self.srt = srt
    self.end = end
    self.v = v
    self.demension = demension

    self.left = None
    self.right = None

    self.lazy_v = 0

  def is_leaf(self):
    '''마지막 노드인가?'''
    return self.left == None and self.right == None

  def set_childs(self, left, right):
    '''자식 노드의 v을 더해서 v에 넣는다. v가 트리일땐, 트리 덧셈을 수행'''
    self.left = left
    self.right = right

    if isinstance(left.v, Node):
      self.v = add_node(left.v, right.v)
    else:
      self.v = left.v + right.v

  def add_v(self, srts, ends, degree):
    '''degress 더하기
    - srts: 업데이트 할 시작 범위
    - ends: 업데이트 할 끝 범위
    '''

    # 범위 조절
    srts = srts[::]
    srts[self.demension] = max(srts[self.demension], self.srt)

    ends = ends[::]
    ends[self.demension] = min(ends[self.demension], self.end)

    if srts[self.demension] > ends[self.demension]:
      # 탐색 범위가 아님.
      return 0

    if self.demension == DEMENSION_X and self.srt == srts[self.demension] and self.end == ends[self.demension]:
      # 범위가 완전히 같은 경우 -> lazy로 저장
      self.lazy_v += degree
      return degree

    delta_v = 0

    if self.is_leaf():
      delta_v += degree
    else:
      delta_v += self.left.add_v(srts, ends, degree)
      delta_v += self.right.add_v(srts, ends, degree)

    if isinstance(self.v, Node):
      # 다음 차원이 있다면 다음 차원으로 넘김
      self.v.add_v(srts, ends, delta_v)
    else:
      self.v += delta_v
    
    return delta_v
    
  def update_v(self):
    '''self.lazy_v를 하위 노드에게 전파'''

    if isinstance(self.v, Node):
      # 다음 차원이 있다면 다음 차원으로 넘김
      self.v.lazy_v += self.lazy_v
      self.v.update_v()
    else:
      self.v += self.lazy_v

    if not self.is_leaf():
      self.left.lazy_v += self.lazy_v
      self.left.update_v()
      self.right.lazy_v += self.lazy_v
      self.right.update_v()

    self.lazy_v = 0

  def get_positive_cnt(self):
    '''트리 내 양수 개수 구하기'''

    if self.is_leaf():
      if isinstance(self.v, Node):
        # 다음 차원이 있다면 다음 차원으로 넘김
        return self.v.get_positive_cnt()
      else:
        return self.v > 0
    else:
      return self.left.get_positive_cnt() + self.right.get_positive_cnt()

def add_node(node_a: Node, node_b: Node):
  '''node_a와 node_b를 더한다. (자식노드들도 더한다)'''
  assert node_a.srt == node_b.srt and node_a.end == node_b.end and node_a.demension == node_b.demension

  node = Node(node_a.srt, node_a.end, node_a.v + node_b.v, node_a.demension)
  if not node_a.is_leaf():
    node.set_childs(add_node(node_a.left, node_b.left), add_node(node_a.right, node_b.right))

  return node

def make_tree(srt, end, arr, demension):
  '''arr값을 트리화'''

  if srt == end:
    # leaf
    return Node(srt, end, arr[srt], demension)
  
  # ! 트리에서 mid = (srt+end) // 2 는 좋은 방법이 아니다. 오른쪽 부터 채우게 된다.
  mid = srt + (end - srt) // 2

  node = Node(srt, end, 0, demension)
  node.set_childs(make_tree(srt, mid, arr, demension), make_tree(mid+1, end, arr, demension))

  return node
  
def solution(board, skill):
  # 1차원 트리 여러개 만듦 y별로 트리가 만들어짐
  # demension x
  row_trees = []
  for row in board:
    tree = make_tree(0, len(row)-1, row, DEMENSION_X) 
    row_trees.append(tree)

  # 1차원 트리를 트리화 함.
  # demension y
  tree_2d = make_tree(0, len(row_trees)-1, row_trees, DEMENSION_Y)

  for type, r1, c1, r2, c2, degree in skill:
    tree_2d.add_v([r1,c1], [r2,c2], degree if type == 2 else - degree)
  tree_2d.update_v()

  return tree_2d.get_positive_cnt()