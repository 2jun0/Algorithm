def dfs(triangle, lv, idx, max_nums):
    if max_nums[lv][idx] != -1:
        return max_nums[lv][idx]
    
    max_num = triangle[lv][idx]
    
    if lv+1 < len(triangle):
        for nxt_idx in [idx+1, idx]:
            max_num = max(max_num, triangle[lv][idx]+dfs(triangle, lv+1, nxt_idx, max_nums))
        
    max_nums[lv][idx] = max_num
    return max_num

def solution(triangle):
    return dfs(triangle, 0, 0, [[-1]*len(line) for line in triangle])