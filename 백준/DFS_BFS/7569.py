"""
1. 아이디어 
- 3차원 배열 지정 -> 동시 방문하면서 +1,  
- dfs로 모든 그래프 돌아다님

2. 시간복잡도
- O(v+e)
- v : 100 * 100 * 100
- e : 100 * 100 * 100 * 4 + 100
- v+e : 5*100^3 => 1000000(100만) < 2억 -> 가능!

3. 자료구조
- bfs -> queue
- 3차원 배열 : int[][][]
- 방문 배열 : bool[][][]
- day : int
"""

import sys

input = sys.stdin.readline

x, y, h = map(int, input().split())
get_data = [list(map(int, input().split())) for _ in range(y * h)]
MAP = [[] for _ in range(h)]

for i in range(h):
    for j in range(i * y, i * y + y):
        MAP[i].append(get_data[j])


# dfs
dx = [0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]
dh = [0, 0, 0, 0, 1, -1]


def bfs():
    while q:
        eh, ey, ex = q.pop(0)
        for k in range(6):
            nh = eh + dh[k]
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= nh < h and 0 <= ny < y and 0 <= nx < x:
                if MAP[nh][ny][nx] == 0:

                    MAP[nh][ny][nx] = MAP[eh][ey][ex] + 1
                    q.append((nh, ny, nx))


q = list()
for i in range(h):
    for j in range(y):
        for k in range(x):
            if MAP[i][j][k] == 1:

                q.append((i, j, k))

bfs()
day = 0
default = False
for i in range(h):
    for j in range(y):
        for k in range(x):
            if not MAP[i][j][k]:
                default = True
            else:
                day = max(day, MAP[i][j][k])

if default:
    print(-1)
else:
    print(day - 1)

for i in MAP:
    print(i)
    print("-" * 10 * x)

# 5 1 7
# 1 0 0 0 0
# 0 0 0 -1 0
# -1 -1 0 0 0
# 0 0 1 -1 0
# -1 -1 0 0 0
# 0 0 0 -1 0
# 1 0 0 0 0
