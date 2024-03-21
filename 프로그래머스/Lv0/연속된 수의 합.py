# 문제 설명
# 연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 두 정수 num과 total이 주어집니다.
# 연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.

# 제한사항
# 1 ≤ num ≤ 100
# 0 ≤ total ≤ 1000
# num개의 연속된 수를 더하여 total이 될 수 없는 테스트 케이스는 없습니다.
# 입출력 예
# num	total	result
# 3	12	[3, 4, 5]
# 5	15	[1, 2, 3, 4, 5]
# 4	14	[2, 3, 4, 5]
# 5	5	[-1, 0, 1, 2, 3]
# 입출력 예 설명
# 입출력 예 #1

# num = 3, total = 12인 경우 [3, 4, 5]를 return합니다.
# 입출력 예 #2

# num = 5, total = 15인 경우 [1, 2, 3, 4, 5]를 return합니다.
# 입출력 예 #3

# 4개의 연속된 수를 더해 14가 되는 경우는 2, 3, 4, 5입니다.
# 입출력 예 #4

# 설명 생략
# solution.py
# 1
# def solution(num, total):
# 2
#     answer = []
# 3
#     return answer
# 실행 결과
# 실행 결과가 여기에 표시됩니다.

from functools import reduce


def solution(num, total):
    answer = []
    sum, start = 0, 0
    randomNumber = [i for i in range(-1000, 1000)]
    while True:
        sum = reduce(lambda acc, cur: acc + cur, randomNumber[start:num])
        if sum == total:
            break
        start += 1
        num += 1
    answer = randomNumber[start:num]
    print(answer)
    return answer


solution(3, 12)
solution(5, 15)
solution(4, 14)
solution(5, 5)
solution(3, 0)
solution(1, 5)
