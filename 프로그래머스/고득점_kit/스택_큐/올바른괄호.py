# 올바른 괄호
# 문제 설명
# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다.
# 예를 들어

# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고,
# 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 문자열 s의 길이 : 100,000 이하의 자연수
# 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
# 입출력 예
# s	answer
# "()()"	true
# "(())()"	true
# ")()("	false
# "(()("	false


def solution(arr):
    A = [arr[0]]  # 초기값

    for i in range(1, len(arr)):
        value = arr[i]
        # ()가 만나면 스택에서 삭제한다.
        if value == ")" and A[-1] == "(":
            A.pop()
        else:
            # stack에 하나 씩 넣는다.
            A.append(value)

    # 스택이 비어지면 True, 남아잇으면 False
    return False if A else True


def solution(s):
    stack = []
    top = -1
    # 1. 배열 반복하면서 stack에 삽입
    for value in s:
        stack.append(value)
        top += 1
        if len(stack) == 1:
            continue
        delete_text = stack[top - 1] + value
        # 2. ()가 만들어지면 삭제
        if delete_text == "()":
            stack.pop(-1)
            stack.pop(-1)
            top -= 2

    # 3. stack의 길이가 0이면 True // 1이면 False
    print(True if len(stack) == 0 else False)
    return True if len(stack) == 0 else False


solution("()()")
solution("(())()")
solution(")()(")
solution('"(()("')
