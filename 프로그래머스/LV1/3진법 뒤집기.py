# 3진법 뒤집기
# 문제 설명
# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후,
# 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# n은 1 이상 100,000,000 이하인 자연수입니다.
# 입출력 예
# n	result
# 45	7
# 125	229


def solution(n):
    # int('3진법', 3) -> 10진수 변환
    result = ""
    while n:
        result += str(n % 3)
        n = n // 3
    print(int(result, 3))
    return int(result, 3)


solution(45)
solution(125)
