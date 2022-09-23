function solution(people, limit) {
  /**
   * 뚱뚱한 사람 먼저
   * 마른 사람은 뚱뚱한 태우고 사람 남는 곳에 탄다고 생각
   */

  people.sort((a, b) => a - b)

  let cnt = 0
  let sum = 0
  let left = 0
  let right = people.length - 1
  /** 뒤가 뚱뚱하니까 뒤 부터 넣어야 됨 */
  while (left <= right) {
    while (left <= right && sum + people[right] <= limit) {
      // 뚱뚱한 사람 최대한 넣자
      sum += people[right]
      right -= 1
    }

    while (left <= right && sum + people[left] <= limit) {
      // 남은 자리에 마른 사람 최대한 넣자
      sum += people[left]
      left += 1
    }

    if (sum > 0) {
      cnt += 1
      sum = 0
    }
  }

  return cnt
}
