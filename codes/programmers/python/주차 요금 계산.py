from math import ceil

def get_fee(_fees, during_time):
  '''요금 계산'''
  DEFAULT_TIME, DEFAULT_FEE, UNIT_TIME, UNIT_FEE = _fees

  fee = DEFAULT_FEE

  if during_time-DEFAULT_TIME > 0:
    fee += ceil((during_time-DEFAULT_TIME)/UNIT_TIME)*UNIT_FEE
  
  return fee

def solution(fees, records):
  record_by_car_num = {}

  for record in records:
    time_str, car_num, in_out = record.split(' ') 

    time_m = 60*int(time_str[:2]) + int(time_str[-2:])

    if car_num not in record_by_car_num:
      # 최초 레코드
      record_by_car_num[car_num] = []

    record_by_car_num[car_num].append((time_m, in_out))

  '''차량 번호 별 요금 구하기'''
  total_fees = []
  for car_num in sorted(list(record_by_car_num.keys())):
    total_during_time = 0

    last_in_time = -1

    for time_m, in_out in record_by_car_num[car_num]:
      if in_out == 'IN':
        last_in_time = time_m
      elif in_out == 'OUT':
        total_during_time += time_m - last_in_time
        last_in_time = -1
    
    if last_in_time != -1:
      # 출차를 안한 경우 -> 23:59에 출차된 걸로 간주
      total_during_time += 23*60+59 - last_in_time
    
    total_fees.append(get_fee(fees, total_during_time))

  return total_fees