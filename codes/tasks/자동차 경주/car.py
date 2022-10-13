from random import randint

class Car:
  def __init__(self):
    self.pos = 0

  def move(self):
    '''한칸 움직임'''
    self.pos += 1
    
  def can_move_randomly(self, threshold = 4):
    '''threshold의 확률로 랜덤하게 움직일 수 있는가?
    - threshold는 [0, 9] 범위이며, 클수록 확률이 높음
    '''
    random_v = randint(0,9)
    return random_v >= threshold
  
  def show_result(self):
    '''실행결과를 보여줌'''
    print('-'*self.pos)