# 문제 설명
# 자연수 n이 매개변수로 주어집니다.
# n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요.
# 답이 항상 존재함은 증명될 수 있습니다.

# 제한사항
# 3 ≤ n ≤ 1,000,000
# 입출력 예
# n	result
# 10	3
# 12	11
def solution(n):
    print(list(filter(lambda x: n % x == 1, range(1, n)))[0])
    return list(filter(lambda x: n % x == 1, range(1, n)))[0]


# 리스트 내포 for 사용법
# return [x for x in range(1,n+1) if n%x==1][0]


solution(10)
solution(12)
