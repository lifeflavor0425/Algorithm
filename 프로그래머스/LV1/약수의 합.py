# 문제 설명
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

# 제한 사항
# n은 0 이상 3000이하인 정수입니다.
# 입출력 예
# n	return
# 12	28
# 5	6
def solution(n):
    answer = 0
    for number in range(1, n + 1):
        answer += number if n % number == 0 else 0
    print(answer)
    return answer


# 자기자신 =>num + 최소 2로 나눈 값부터 개수 구하면 됨
# def sumDivisor(num):
#     # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
#     return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
solution(12)
solution(5)
