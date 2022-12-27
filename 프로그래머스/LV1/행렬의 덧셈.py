# 행렬의 덧셈
# 문제 설명
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
# 입출력 예
# arr1	arr2	return
# [[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
# [[1],[2]]	[[3],[4]]	[[4],[6]]
# arr1 : [[1, 2, 3, 4], [4, 5, 6, 7], [1, 2, 3, 3]]
# arr2 : [[3, 2, 1, 5], [6, 5, 4, 9], [4, 5, 6, 7]]
# answer : [[4, 4, 4, 9], [10, 10, 10, 16], [5, 7, 9, 10]]


def solution(arr1, arr2):
    answer = []
    tmp = []
    for num1, num2 in zip(arr1, arr2):
        for index in range(len(num1)):
            tmp.append(num1[index] + num2[index])
        answer.append(tmp)
        tmp = []
    print(answer)
    return answer
    # 한줄
    # answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]


solution([[1, 2], [2, 3]], [[3, 4], [5, 6]])
solution([[1], [2]], [[3], [4]])
solution([[1, 2, 3, 4], [4, 5, 6, 7], [1, 2, 3, 3]], [[3, 2, 1, 5], [6, 5, 4, 9], [4, 5, 6, 7]])
