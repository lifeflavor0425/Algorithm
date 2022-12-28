# 최대공약수와 최소공배수
# 문제 설명
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
# 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
# 예를 들어 두 수 3, 12의 최대공약수는 3,
# 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

# 제한 사항
# 두 수는 1이상 1000000이하의 자연수입니다.
# 입출력 예
# n	m	return
# 3	12	[3, 12]
# 2	5	[1, 10]


def solution(n, m):
    max_number = max([i for i in range(min(n, m), 0, -1) if n % i == 0 and m % i == 0])
    min_number = min([i for i in range(max(n, m), n * m + 1) if i % n == 0 and i % m == 0])
    print([max_number, min_number])
    return [max_number, min_number]
    # 최대공약수 함수 gcd , 최소공배수 함수 lcm
    # gcd = lambda a, b: b if not a % b else gcd(b, a % b)
    # lcm = lambda a, b: a * b // gcd(a, b)
    # print([gcd(n, m), lcm(n, m)])
    # return [gcd(n, m), lcm(n, m)]


solution(3, 12)
solution(2, 5)
