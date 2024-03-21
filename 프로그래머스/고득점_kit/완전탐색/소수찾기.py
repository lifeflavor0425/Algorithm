"""
소수 찾기
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
"17"	3
"011"	2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.
"""

from itertools import permutations


def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    print(a)
    a -= set(range(0, 2))
    print(a)
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    print(a)
    return len(a)


# import math
# from itertools import combinations, permutations
# def solution(numbers):
#     answer = 0

#     # 최대값 구하기
#     Max_number = int("".join(sorted(list(numbers),reverse=True)))
#     sosu_list = [i for i in range(Max_number+1)]
#     # 소수 축출
#     sosu(Max_number, sosu_list)
#     # 각 자리수로 시작하는 숫자 리스트 만들기
#     A = [[] for _ in range(len(numbers) + 1)]
#     for i in range(1,len(numbers)+1):
#         tmp_list = list(permutations(numbers, i))
#         for j in tmp_list:
#             str_j = int("".join(list(j)))
#             if str_j in A[i] or len(str(str_j)) != i:
#                 continue
#             if str_j > 1 :
#                 A[i].append(str_j)

#     # 소수가 있는지 확인하고 count +
#     for i in range(1, len(A)):
#         tmp_list = A[i]
#         for j in range(2,len(sosu_list)):
#             if not sosu_list[j] :
#                 continue
#             if len(str(sosu_list[j])) > i:
#                 continue
#             if sosu_list[j] in tmp_list :
#                 answer += 1

#     return answer


# # 소수 구하는 함수
# def sosu(Max_number, sosu_list):
#     for i in range(2, int(math.sqrt(Max_number)) + 1):
#         if sosu_list[i] == 0:
#             continue
#         for j in range(i+i, Max_number+1, i):
#             sosu_list[j]=0
