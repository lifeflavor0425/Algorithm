# 소수 찾기
# 문제 설명
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)

# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.
# 입출력 예
# n	result
# 10	4
# 5	3


# def solution(n):
#     answer = 0
#     for i in range(2, n + 1):
#         if is_prime_number(i):
#             answer += 1
#     print(answer)
#     return answer


# import math

# # 소수 판별 함수
# def is_prime_number(x):
#     # 2부터 x의 제곱근까지의 모든 수를 확인하며
#     for i in range(2, int(math.sqrt(x)) + 1):
#         # x가 해당 수로 나누어떨어진다면
#         if x % i == 0:
#             return False  # 소수가 아님
#     return True  # 소수임


# 에라토스테네스의 체 ******
def solution(n):
    num = set(range(2, n + 1))
    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    print(len(num))
    return len(num)


solution(10)
solution(5)
