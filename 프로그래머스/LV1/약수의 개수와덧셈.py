# 약수의 개수와 덧셈
# 문제 설명
# 두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서,
# 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를
# return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ left ≤ right ≤ 1,000
# 입출력 예
# left	right	result
# 13	17	43
# 24	27	52


def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        answer += (
            num
            if (len([index for index in range(1, num // 2 + 1) if num % index == 0]) + 1) % 2 == 0
            else -num
        )
    print(answer)
    return answer
    # 제곱수인 숫자의 약수는 홀수가 나오고, 제곱수가 아닌 숫자의 약수는 짝수가 나온다.
    # answer = 0
    # for i in range(left, right + 1):
    #     if int(i**0.5) == i**0.5:
    #         answer -= i
    #     else:
    #         answer += i
    # print(answer)
    # return answer


solution(13, 17)
solution(24, 27)
