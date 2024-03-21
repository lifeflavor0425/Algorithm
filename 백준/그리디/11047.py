"""
1. 아이디어
- 동전을 저장한뒤, 반대로 뒤집음
- 동전 for 
    - 동전 사용 개수 추가
    - 동전 사용한만큼 k값 갱신
2. 시간복잡도
- O(n)

3. 자료구조
- 동전 금액 : int[]
- 동전 사용 개수 : int
- 남은 금액 : int
"""

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
ARR = [int(input()) for _ in range(N)]
cnt = 0
ARR.reverse()
for i in ARR:
    if K < i:
        continue
    tmp = K // i
    cnt += tmp
    K %= i

print(cnt)
