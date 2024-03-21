# 문제
# DFS 와 BFS로 탐색한 결과를 출력하라
# 단,방문할 수 있을 정점이 여러 개인 경우 번호가 작은 것 부터 방문
# 1~ n

# 준비
# BFS -> QUeue / DFS -> Stack
# O(v+e)
# v : 1000
# E : 10000

import sys

input = sys.stdin.readline
# 데이터 준비
n, m, first = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(m)]
e_arr = [list() for _ in range(n + 1)]

chk_DFS = [False] * (n + 1)
chk_BFS = [False] * (n + 1)
for a, b in MAP:
    e_arr[a].append(b)
    e_arr[b].append(a)

for i in range(1, n + 1):
    e_arr[i].sort()

# DFS
rs_DFS = list()


def DFS(v):
    chk_DFS[v] = True
    rs_DFS.append(v)
    for i in e_arr[v]:
        if chk_DFS[i] == False:
            DFS(i)


# BFS
def BFS(first):
    q = [first]
    rs_bfs = list()
    while q:
        visit = q.pop(0)
        chk_BFS[visit] = True
        rs_bfs.append(visit)
        for i in e_arr[visit]:
            if chk_BFS[i] == False:
                chk_BFS[i] = True
                q.append(i)
    return rs_bfs


DFS(first)
for i in range(len(rs_DFS)):
    print(rs_DFS[i], end=" ")
print()
for i in BFS(first):
    print(i, end=" ")
