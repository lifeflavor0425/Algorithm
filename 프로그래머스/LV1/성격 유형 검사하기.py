# 문제 설명
# 나만의 카카오 성격 유형 검사지를 만들려고 합니다.
# 성격 유형 검사는 다음과 같은 4개 지표로 성격 유형을 구분합니다. 성격은 각 지표에서
# 두 유형 중 하나로 결정됩니다.

# 지표 번호	성격 유형
# 1번 지표	라이언형(R), 튜브형(T)
# 2번 지표	콘형(C), 프로도형(F)
# 3번 지표	제이지형(J), 무지형(M)
# 4번 지표	어피치형(A), 네오형(N)

# 입출력 예
# survey	choices	result
# ["AN", "CF", "MJ", "RT", "NA"]	[5, 3, 2, 7, 5]	"TCMA"
# ["TR", "RT", "TR"]	[7, 1, 3]	"RCJA"


def solution(survey, choices):
    answer = ""
    # 1. 성격 유형 배열 딕셔너리 선언
    MBTI = [
        {"R": 0, "T": 0},
        {"C": 0, "F": 0},
        {"J": 0, "M": 0},
        {"A": 0, "N": 0},
    ]
    # 1-2. 문제 유형 dict 선언
    problem_dict = {"TR": 0, "RT": 0, "CF": 1, "FC": 1, "JM": 2, "MJ": 2, "NA": 3, "AN": 3}
    # 2. survey 와 choice 동시 반복
    for problem, choice in zip(survey, choices):
        idx = problem_dict[problem]
        if choice == 4:
            continue
        elif choice == 1 or choice == 2 or choice == 3:
            text = problem[0]
            MBTI[idx][text] += abs(choice - 4)
        else:
            text = problem[1]
            MBTI[idx][text] += choice - 4
    # 3. mbti의 각 dict 안에서 높은값 출력, 값이 같으면 사전순 높은것 출력
    for idx, (key, value) in enumerate(MBTI):
        tmp = key if MBTI[idx][key] >= MBTI[idx][value] else value
        answer += tmp
    print(MBTI)
    print(answer)
    return answer


solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
solution(["TR", "RT", "TR"],	[7, 1, 3])