# 문제
# N×M크기의 배열로 표현되는 미로가 있다.
# 1은 이동 가능, 0은 불가능 칸
# (1,1) 에서 출발 -> (n,m)의 위치로 이동
# 2< n, m < 100

"""
1. 아이디어
- 2중 for -> 값 1 && 방문 x -> BFS
- BFS 하면서 카운트 ++

2. 시간 복잡도
- O(V+E)
- V : n*m
- E : n*m*4
- 5n*m -> 50000 < 2억 >> 가능!

3. 자료구조
- 2중 리스트 : int[][]
- 방문 리스트 : bool[][]
- 카우트 값 : int
"""

import sys

sys.setrecursionlimit(15000)
input = sys.stdin.readline
n, m = map(int, input().split())
MAP = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]
# BFS
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(y, x):
    q = [(y, x)]
    while q:
        ey, ex = q.pop(0)

        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if MAP[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    MAP[ny][nx] = MAP[ey][ex] + 1
                    q.append((ny, nx))


chk[0][0] = True
bfs(0, 0)
print(MAP[n - 1][m - 1])
