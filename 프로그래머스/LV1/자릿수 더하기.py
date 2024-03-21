# 문제 설명
# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

# 제한사항
# N의 범위 : 100,000,000 이하의 자연수
# 입출력 예
# N	answer
# 123	6
# 987	24
def solution(n):
    answer = 0
    text = str(n)
    for num in text:
        answer += int(num)
    print(answer)
    # 1줄
    # answer = sum([int(i) for i in str(n)])
    return answer


solution(123)
solution(987)
