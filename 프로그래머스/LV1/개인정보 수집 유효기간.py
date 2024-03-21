# 문제 설명
# 고객의 약관 동의를 얻어서 수집된 1~n번으로 분류되는 개인정보 n개가 있습니다. 약관 종류는 여러 가지 있으며
# 각 약관마다 개인정보 보관 유효기간이 정해져 있습니다. 당신은 각 개인정보가 어떤 약관으로 수집됐는지 알고 있습니다.
# 수집된 개인정보는 유효기간 전까지만 보관 가능하며, 유효기간이 지났다면 반드시 파기해야 합니다.

# 예를 들어, A라는 약관의 유효기간이 12 달이고, 2021년 1월 5일에 수집된 개인정보가 A약관으로 수집되었다면
# 해당 개인정보는 2022년 1월 4일까지 보관 가능하며 2022년 1월 5일부터 파기해야 할 개인정보입니다.
# 당신은 오늘 날짜로 파기해야 할 개인정보 번호들을 구하려 합니다.

# 모든 달은 28일까지 있다고 가정합니다.

# 다음은 오늘 날짜가 2022.05.19일 때의 예시입니다.

# 약관 종류	유효기간
# A	6 달
# B	12 달
# C	3 달
# 번호	개인정보 수집 일자	약관 종류
# 1	2021.05.02	A
# 2	2021.07.01	B
# 3	2022.02.19	C
# 4	2022.02.20	C

# 입출력 예
# today	terms	privacies	result
# "2022.05.19"	["A 6", "B 12", "C 3"]	["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]	[1, 3]
# "2020.01.01"	["Z 3", "D 5"]	["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]	[1, 4, 5]


def solution(today, terms, privacies):
    answer = []
    # 1. terms와 privacies 를 딕셔너리로 만들기
    terms_dict = {value.split()[0]: int(value.split()[1]) * 28 for value in terms}
    print(terms_dict)
    t_year,t_month,t_day = today.split('.')
    today = int(t_year)*12*28 + int(t_month)*28 + int(t_day)
    print(today)
    for idx, p in enumerate(privacies):
        year, month, day= p.split('.')
        day, term = day.split()
        end = int(year)*12*28 + int(month)*28 + int(day) 
        print(end)
        if end + terms_dict[term] <= today:
            answer.append(idx + 1)
    print(answer)
    return answer


# def solution(today, terms, privacies):
#     answer = []
#     terms_dic = {term.split(" ")[0]: int(term.split(" ")[1]) * 28 for term in terms}
#     t_y, t_m, t_d = today.split(".")
#     today = int(t_y) * 12 * 28 + int(t_m) * 28 + int(t_d)
#     print(today)
#     print(terms_dic)
#     for idx, p in enumerate(privacies):
#         year, month, day = p.split(".")
#         day, term = day.split(" ")
#         print(day, term)
#         check_day = int(year) * 12 * 28 + int(month) * 28 + int(day)

#         if check_day + terms_dic[term] <= today:
#             answer.append(idx + 1)
#     print(answer)
#     return answer


# solution(
#     "2022.05.19",
#     ["A 6", "B 12", "C 3"],
#     ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"],
# )
solution(
    "2020.01.01",
    ["Z 3", "D 5"],
    ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"],
)

# solution("2022.02.28" ,  ["A 23"],   ["2020.01.28 A"]) # [1]
# solution("2019.01.01", ["B 12"], ["2017.12.21 B"])
# terms =  ["B 12"]
# privacies = ["2017.12.21 B"]
# today = "2019.01.01"
# 을 넣어보시면 될 것 같습니다...!
# 답은 계약기간은 2018.12.21이 되고 현재는 2019.01.01 이기 때문에 1이 나와야합니다.
