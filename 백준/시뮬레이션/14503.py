"""
1. 아이디어
- 특정 조건을 만족하는 한 계속 이동 > while
- 4방향 탐색 먼저 수행 > 빈칸 있을 경우 이동
- 4방향 탐색 안될 경우, 뒤도 한칸 가서 반복

2. 시간복잡도
- 좌표 n*m, 주변값 4 -> n*m*4
- O(n*m)
- 50^2 = 2500 < 2억 -> 가능!
3. 자료구조
- 전체 지도 : int[][] -> 0:청소, 1:벽, 2:청소O
- 내 위치, 방향 : int, int, int
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
while 1:
    if MAP[y][x] == 0:
        MAP[y][x] = 2
        cnt += 1
    sw = False
    for i in range(1, 5):
        ny = y + dy[(d - i + 4) % 4]
        nx = x + dx[(d - i + 4) % 4]
        if 0 <= ny < N and 0 <= nx < M:
            if MAP[ny][nx] == 0:
                d = (d - i + 4) % 4
                y = ny
                x = nx
                sw = True
                break

    if sw == False:
        ny = y - dy[d]
        nx = x - dx[d]
        if 0 <= ny < N and 0 <= nx < M:
            if MAP[ny][nx] == 1:
                break
            else:
                y = ny
                x = nx
        else:
            break
print(cnt)
