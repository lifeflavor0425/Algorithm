# 겹치는 선분의 길이
# 문제 설명
# 선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]]
# 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.

# lines가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.
# 선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 길이 2만큼 겹쳐있습니다.

# 제한사항
# lines의 길이 = 3
# lines의 원소의 길이 = 2
# 모든 선분은 길이가 1 이상입니다.
# lines의 원소는 [a, b] 형태이며, a, b는 각각 선분의 양 끝점 입니다.
# -100 ≤ a < b ≤ 100
# 입출력 예
# lines	result
# [[0, 1], [2, 5], [3, 9]]	2
# [[-1, 1], [1, 3], [3, 9]]	0
# [[0, 5], [3, 9], [1, 10]]	8


def solution(lines):
    answer = 0
    s = []
    for index in range(len(lines)):
        s.append([x for x in range(lines[index][0], lines[index][1] + 1)])
    # print(s)
    s1 = set(s[0]) & set(s[1])
    s2 = set(s[1]) & set(s[2])
    s3 = set(s[0]) & set(s[2])
    s = [] if len(s1) <= 1 and len(s2) <= 1 and len(s3) <= 1 else list(s1 | s2 | s3)
    # answer = length(s1) + length(s2) + length(s3)
    answer = length(s)
    return answer


def length(array):
    if len(array) < 2:
        return 0
    return len(array) - 1


# def solution(lines):
#     answer = 0

#     last_dot = max(lines[0][1],lines[1][1],lines[2][1])
#     first_dot = min(lines[0][0],lines[1][0],lines[2][0])

#     f_sector = [[i,i+1] for i in range(lines[0][0],lines[0][1])]
#     s_sector = [[j,j+1] for j in range(lines[1][0],lines[1][1])]
#     t_sector = [[k,k+1] for k in range(lines[2][0],lines[2][1])]
#     total_sector = [[x,x+1] for x in range(first_dot, last_dot)]
#     count_dict = {y:0 for y in range(first_dot, last_dot)}

#     for sec in total_sector:
#         count_dict[sec[0]] += f_sector.count(sec)
#         count_dict[sec[0]] += s_sector.count(sec)
#         count_dict[sec[0]] += t_sector.count(sec)

#     for k,v in count_dict.items():
#         if v >= 2 :
#             answer += 1

#     return answer

solution([[0, 1], [2, 5], [3, 9]])
solution([[-1, 1], [1, 3], [3, 9]])
solution([[0, 5], [3, 9], [1, 10]])
