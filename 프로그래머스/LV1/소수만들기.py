# 소수 만들기
# 문제 설명
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때,
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때
# 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
# 입출력 예
# nums	result
# [1,2,3,4]	1
# [1,2,7,6,4]	4

from itertools import combinations
def solution(nums):
    answer = 0
    sosu_arr = set(range(2, max(nums) * 3))
    for i in range(2, max(nums) * 3):
        if i in sosu_arr:
            sosu_arr -= set(range(2 * i, max(nums) * 3, i))
    print(sosu_arr)
    for values in combinations(nums, 3) :
        answer += 1 if sum(values) in sosu_arr else 0
    print(answer)
    return answer



solution([1,2,3,4])
solution([1,2,7,6,4])