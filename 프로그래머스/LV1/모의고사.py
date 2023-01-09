# 모의고사
# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
# 입출력 예
# answers	return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]


def solution(answers):

    one_stack = [1, 2, 3, 4, 5]
    two_stack = [2, 1, 2, 3, 2, 4, 2, 5]
    three_stack = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = [
        answer_count(answers, one_stack),
        answer_count(answers, two_stack),
        answer_count(answers, three_stack),
    ]
    if answer.count(max(answer)) > 1:
        dup = [i+1 for i, x in enumerate(answer) if max(answer) == x]
        print(dup)
        return dup
    else:
        print([answer.index(max(answer)) + 1])
        return [answer.index(max(answer)) + 1]

# 런타임 에러 해결법
# 배열을 지속적으로 할당하면 계속 새로운 객체가 할당된다. -> 메모리 포화
def answer_count(answers, stack):
    count = 0
    tmp = stack.copy()
    tmp2 = answers.copy()
    while tmp2:
        if tmp.pop(0) == tmp2.pop(0):
            count += 1
        if not tmp:
            tmp = stack.copy()
    return count


solution([1, 2, 3, 4, 5])
solution([1, 3, 2, 4, 2])
