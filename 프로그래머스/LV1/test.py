# import itertools
# def solution(numbers):
#     nPr = itertools.permutations(numbers, len(numbers))
#     sum_text = ""
#     sum_text_arr = []
#     for arr in list(nPr):
#         sum_text = ""
#         for text in arr:
#             sum_text += str(text)
#         if not sum_text_arr or sum_text_arr[-1] < int(sum_text):
#             sum_text_arr.append(int(sum_text))
#     print(max(sum_text_arr))
#     return str(max(sum_text_arr))
# ====> 경우의 수 너무 많아 런타임 에러

# def solution(numbers):
#     answer = ""
#     text_numbers = [str(text) for text in numbers]
#     while text_numbers:
#         print(max(text_numbers))
#         index = text_numbers.index(max(text_numbers))
#         answer += text_numbers.pop(index)
#     print(answer)
#     return answer
# ===> 30, 3 해결 못함


def solution(numbers):
    numbers_str = [str(num) for num in numbers]
    numbers_str.sort(key=lambda num: num * 3, reverse=True)
    print(numbers_str)
    print("".join(numbers_str))
    return "".join(numbers_str)


solution([6, 10, 2])
solution([3, 30, 34, 5, 9])
solution([0, 0, 0])
