"""
1. 아이디어
- MAP을 돌면서 카운트 ++ -> 방문 여부 확인(중복 때문에) 
- bfs 를 하면서 카운터를 증가

2. 시간 복잡도
- O(v+e)
- v : 100
- e : 100*99 / 2 -> 4950
- v+e : 5000 -> 가능

3. 자료구조
- bfs
- queue : int[]
- 방문 : bool[]
- MAP : int[][]
- 카운트 : int

"""

import sys

input = sys.stdin.readline

n = int(input())
q1, q2 = map(int, input().split())
e = int(input())
MAP = [[] for _ in range(n + 1)]
chk = [False] * (n + 1)
for _ in range(1, e + 1):
    a, b = map(int, input().split())
    MAP[a].append(b)
    MAP[b].append(a)


# bfs
def bfs(start, end):
    q = [start]
    cnt_arr = [0] * (n + 1)
    while q:
        visit = q.pop(0)
        if chk[visit] == False:
            chk[visit] = True
            for i in MAP[visit]:
                cnt_arr[i] = cnt_arr[visit] + 1
                q.append(i)
        if visit == end:
            q.clear()
    return cnt_arr


result = bfs(q1, q2)[q2]
if result:
    print(result)
else:
    print(-1)
