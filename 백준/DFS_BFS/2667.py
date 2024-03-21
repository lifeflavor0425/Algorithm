"""
1. 아이디어
- 2중 for, 값 1 && 방문 x => DFS
- DFS를 통해 찾은 값을 저장 후 정렬 출력

2. 시간 복잡도
- DFS : O(v+e)
- V : n^2, 4n^2
- V + E : 625 >> 가능
3. 자료구조
- 그래프 저장 : int[][]
- 방문 여부 : bool[][]
- 결과값 : int[]
"""

import sys

input = sys.stdin.readline

n = int(input())
MAP = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False] * n for _ in range(n)]
result = []
each = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


# dfs
def dfs(y, x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < n and 0 <= nx < n:
            if MAP[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny, nx)


for i in range(n):
    for j in range(n):
        if MAP[i][j] == 1 and chk[i][j] == False:
            # 방문 체크
            chk[i][j] = True
            each = 0
            # DFS 로 크기 구하기
            dfs(i, j)
            # 크기 결과값에 리스트에 넣기
            result.append(each)
result.sort()
print(len(result))
for i in result:
    print(i)
