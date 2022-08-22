def solution(id_list, report, k):
  # 중복 삭제!
  report = set(report)

  # cnts
  cnts = {id:0 for id in id_list}
  result_by_id = {id:0 for id in id_list}

  for cmd in report:
    from_id, to_id = cmd.split(' ')
    cnts[to_id] += 1

  for cmd in report:
    from_id, to_id = cmd.split(' ')
    if cnts[to_id] >= k:
      result_by_id[from_id] += 1


  # result_by_id를 dict에서 array로 변환
  result_by_idx = [0]*len(id_list)
  for idx, id in enumerate(id_list):
    result_by_idx[idx] = result_by_id[id]

  return result_by_idx