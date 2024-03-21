"""
1. 아이디어
- 1번 출발 ->MAP을 이동하면서 카운트 ++ -> bfs
- 간선 MAP을 이중 리스트로 만듬

2. 자료구조
- bfs
- queue : int[][]
- MAP : int[][]
- 카운트 : int
- 방문 리스트 : bool [][]

3. 시간 복잡도
- O(v+e)
- v : 100
- e : 100 * 99 / 2 -> 4950
- v+e : 5000 -> 가능
"""

import sys

input = sys.stdin.readline

v = int(input())
e = int(input())
MAP = [[] for _ in range(v + 1)]
chk = [False] * (v + 1)

for _ in range(1, e + 1):
    a, b = map(int, input().split())
    MAP[a].append(b)
    MAP[b].append(a)


# bfs
def bfs(v):
    q = [v]
    cnt = 0
    while q:
        visit = q.pop(0)
        if chk[visit] == False:
            chk[visit] = True
            cnt += 1
            for i in MAP[visit]:
                q.append(i)
    return cnt


print(bfs(1) - 1)
