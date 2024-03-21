"""
1.아이디어
- N개의 숫자를 정렬
- M개를 for 돌면서, 이진탐색
- 이진탐색 안에서 마지막에 데이터 찾으면, 1출력, 아니면 0출력

2. 시간복잡도
- N개 입력값 정렬 = O(NlgN)
- M개를 탐색 = O(M*lgN)
- 총합 : O((N*M)lgN) > 가능

3. 자료구조
- N개 숫자 : int[]
- M개 숫자 : int[]
"""

import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

nums.sort()  # 이진 탐색 가능


def search(st, ed, target):
    if st == ed:
        if nums[st] == target:
            print(1)
        else:
            print(0)
        return
    mid = (st + ed) // 2
    if nums[mid] < target:
        search(mid + 1, ed, target)
    else:
        search(st, mid, target)


for each in target_list:
    search(0, N - 1, each)
