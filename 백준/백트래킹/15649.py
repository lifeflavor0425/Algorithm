"""
1. 아이디어
- 백트래킹 재귀함수 안에서 , for 돌면서 숫자 선택(방문 여부 확인)
- 재귀 함수에서 M개를 선택할 경우 print
2. 시간복잡도
- N! > 10까지 -> 가능!
3. 자료구조 
- 결과값 저장 int[]
- 방문여무 체크 
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
rs = []
chk = [False] * (N + 1)


def recur(num):
    if num == M:
        print(" ".join(map(str, rs)))
    for i in range(1, N + 1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num + 1)
            chk[i] = False
            rs.pop()


recur(0)
