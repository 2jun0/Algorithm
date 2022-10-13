import sys
from typing import List

from car import Car

def play(cars: List[Car], turn_cnt: int):
  '''cars들이 turn_cnt번 경주함'''
  print('실행 결과')

  for _ in range(turn_cnt):
    for car in cars:
      if car.can_move_randomly():
        # 자동차가 움직일 수 있으면 움직임 (확률은 기본값)
        car.move()

      car.show_result()
    print()

def main():
  print('자동차 대수는 몇 대 인가요?')
  # 자동차 개수 입력 받고 자동차 객체 생성
  car_cnt = int(sys.stdin.readline().strip())
  cars = [Car() for _ in range(car_cnt)]
  
  # 시도할 회수 입력 받음
  print('시도할 회수는 몇 회인가요?')
  turn_cnt = int(sys.stdin.readline().strip())
  print()

  # 플레이
  play(cars, turn_cnt)

if __name__ == '__main__':
  main()