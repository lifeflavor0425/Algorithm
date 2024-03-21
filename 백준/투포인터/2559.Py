"""
1. 아이디어
- 반복문을 돌면서 리스트 길이 =k 가 되면 최대값을 지정
- 그 후 값들을 빼고 더하면서 최대값 비교
- 리스트 길이 관리
- 투포인터 사용
2. 시간복잡도
- O(N)
- 연속적인 수 -> 한바퀴
3. 자료구조
- 투포인터
- 리스트 관리 : int[]
- 최대값 : int
"""

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
ARR = list(map(int, input().split()))
SUM = 0

for i in range(K):
    SUM += ARR[i]
MAX = SUM

for i in range(K, N):
    SUM += ARR[i]
    SUM -= ARR[i - K]
    MAX = max(SUM, MAX)
print(MAX)
